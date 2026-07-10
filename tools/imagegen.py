#!/usr/bin/env python3
"""WizTryサイトの画像生成 共通ライブラリ。

【会社ルール】生成モデルの優先順位（2026-07-10 末松指示）:
  1. GPT-Image-2      (OpenAI: gpt-image-2)
  2. Nano Banana 2    (Google: gemini-3.1-flash-image)
  3. Nano Banana Pro  (Google: gemini-3-pro-image)
上位が失敗・レート制限のときだけ下位へフォールバックする。

APIキーは ~/.config/wiztry/image-gen.env（OPENAI_API_KEY / GEMINI_API_KEY）から読む。
無ければmacOS KeychainのGEMINI_API_KEYを参照。
"""
import base64, json, os, subprocess, time, urllib.request

ENV_PATH = os.path.expanduser('~/.config/wiztry/image-gen.env')


def _load_keys():
    keys = {}
    if os.path.exists(ENV_PATH):
        for line in open(ENV_PATH):
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                k, v = line.split('=', 1)
                keys[k.strip()] = v.strip().strip('"').strip("'")
    if not keys.get('GEMINI_API_KEY'):
        r = subprocess.run(['security', 'find-generic-password', '-s', 'GEMINI_API_KEY', '-w'],
                           capture_output=True, text=True)
        if r.returncode == 0:
            keys['GEMINI_API_KEY'] = r.stdout.strip()
    return keys


KEYS = _load_keys()

# aspect → (OpenAIサイズ, Gemini aspectRatio)
ASPECT = {
    '16:9': ('1536x1024', '16:9'),
    '4:3': ('1536x1024', '4:3'),
    '1:1': ('1024x1024', '1:1'),
    '3:2': ('1536x1024', '3:2'),
    '9:16': ('1024x1536', '9:16'),
}


def _openai_gpt_image2(prompt, aspect):
    size, _ = ASPECT[aspect]
    body = {'model': 'gpt-image-2', 'prompt': prompt, 'size': size, 'quality': 'high', 'n': 1}
    req = urllib.request.Request(
        'https://api.openai.com/v1/images/generations',
        data=json.dumps(body).encode(),
        headers={'Content-Type': 'application/json', 'Authorization': f"Bearer {KEYS['OPENAI_API_KEY']}"})
    r = json.load(urllib.request.urlopen(req, timeout=300))
    return base64.b64decode(r['data'][0]['b64_json'])


def _gemini(model, prompt, aspect):
    _, ar = ASPECT[aspect]
    body = {'contents': [{'parts': [{'text': prompt}]}],
            'generationConfig': {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': ar}}}
    req = urllib.request.Request(
        f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent',
        data=json.dumps(body).encode(),
        headers={'Content-Type': 'application/json', 'x-goog-api-key': KEYS['GEMINI_API_KEY']})
    r = json.load(urllib.request.urlopen(req, timeout=300))
    for p in r['candidates'][0]['content']['parts']:
        if 'inlineData' in p:
            return base64.b64decode(p['inlineData']['data'])
    raise RuntimeError('no image part')


PROVIDERS = [
    ('gpt-image-2', lambda pr, ar: _openai_gpt_image2(pr, ar), 'OPENAI_API_KEY'),
    ('gemini-3.1-flash-image', lambda pr, ar: _gemini('gemini-3.1-flash-image', pr, ar), 'GEMINI_API_KEY'),
    ('gemini-3-pro-image', lambda pr, ar: _gemini('gemini-3-pro-image', pr, ar), 'GEMINI_API_KEY'),
]


def generate(prompt, aspect='16:9', retries_per_provider=2):
    """優先順位に従い生成し、(bytes, 使用モデル名) を返す。全滅なら例外。"""
    last = None
    for name, fn, keyname in PROVIDERS:
        if not KEYS.get(keyname):
            continue
        for attempt in range(retries_per_provider):
            try:
                return fn(prompt, aspect), name
            except Exception as e:
                last = e
                time.sleep(6 * (attempt + 1))
    raise RuntimeError(f'all providers failed: {last}')


if __name__ == '__main__':
    import sys
    data, model = generate(sys.argv[1] if len(sys.argv) > 1 else 'a glowing blue cube on navy background, minimal', '1:1')
    open('/tmp/imagegen-test.png', 'wb').write(data)
    print('OK', model, len(data), '-> /tmp/imagegen-test.png')
