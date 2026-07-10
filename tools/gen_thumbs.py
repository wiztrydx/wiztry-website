#!/usr/bin/env python3
"""ブログサムネイルを画像生成（gemini-3-pro-image / Nano Banana Pro）で作る。

タイトルのキーワードを画像内に直接描画させる。日本語の誤字が出ることがあるので、
生成後は必ず目視チェックし、誤字があれば該当slugだけ再実行する。
WizTryロゴは正確性のため生成後にPILで合成する。

usage: python3 tools/gen_thumbs.py [slug ...]   # 引数なしで thumbs_config.json 全件
       FORCE=1 を付けると既存ファイルがあっても再生成
"""
import json, os, sys, base64, subprocess, time, urllib.request
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'public', 'thumbs')
os.makedirs(OUT, exist_ok=True)

KEY = subprocess.run(['security', 'find-generic-password', '-s', 'GEMINI_API_KEY', '-w'],
                     capture_output=True, text=True).stdout.strip()
API = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image:generateContent'

TEMPLATE = """Design a premium blog thumbnail image for a Japanese AI company's corporate blog.

Art direction: deep navy blue (#0a1630) background, {theme}, electric blue (#2f6bff) and cyan (#37c8f0) glowing light accents, clean sophisticated modern Japanese web design, generous margins, cinematic lighting.

Typography — render EXACTLY these characters with no typos, no missing or extra characters. NEVER draw quotation marks or the corner brackets 「」 — they only mark the boundaries of the text in this prompt. If the text contains the character "|", start a new line exactly at that position (do not draw the "|" itself):
- Main title, very large, extra-bold white Japanese gothic (sans-serif) font, left-aligned: 「{main}」
- Below it, smaller sub text in light cyan: 「{sub}」
No other stray text, smudged letters or pseudo-text anywhere else in the image.

The text block sits on the left side with high contrast against a darkened area. Text must be crisp and easily readable even at small sizes. Absolutely no other words, letters, numbers, logos or watermarks anywhere in the image. Keep the lower-left corner area relatively clear (a logo will be placed there later)."""


def generate(entry, retries=2):
    slug = entry['slug']
    out = os.path.join(OUT, f'{slug}.webp')
    if os.path.exists(out) and not os.environ.get('FORCE') and slug not in sys.argv[1:]:
        print('skip', slug)
        return
    prompt = TEMPLATE.format(theme=entry['theme'], main=entry['main'], sub=entry['sub'])
    body = {
        'contents': [{'parts': [{'text': prompt}]}],
        'generationConfig': {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': '16:9'}},
    }
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(API, data=json.dumps(body).encode(),
                                         headers={'Content-Type': 'application/json', 'x-goog-api-key': KEY})
            r = json.load(urllib.request.urlopen(req, timeout=300))
            for p in r['candidates'][0]['content']['parts']:
                if 'inlineData' in p:
                    raw = base64.b64decode(p['inlineData']['data'])
                    tmp = os.path.join(OUT, f'{slug}.tmp.png')
                    open(tmp, 'wb').write(raw)
                    finish(tmp, out)
                    os.remove(tmp)
                    print('OK', slug)
                    return
            raise RuntimeError('no image part')
        except Exception as e:
            print(f'retry {slug} ({attempt + 1}): {str(e)[:100]}')
            time.sleep(8)
    print('FAIL', slug)


def finish(src, out):
    """1200x675に整形し、本物のWizTry白ロゴを左下に合成"""
    im = Image.open(src).convert('RGB')
    im = im.resize((1200, int(im.height * 1200 / im.width)), Image.LANCZOS)
    if im.height != 675:
        top = max((im.height - 675) // 2, 0)
        im = im.crop((0, top, 1200, top + 675))
    logo = Image.open(os.path.join(ROOT, 'public', 'logos', 'wiztry-logo-white.png'))
    lw = 170
    lh = int(logo.height * lw / logo.width)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    im.paste(logo, (72, 675 - lh - 48), logo)
    im.save(out, 'WEBP', quality=85)


defs = json.load(open(os.path.join(ROOT, 'tools', 'thumbs_config.json')))
targets = sys.argv[1:]
for e in defs:
    if not targets or e['slug'] in targets:
        generate(e)
