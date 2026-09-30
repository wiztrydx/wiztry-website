#!/usr/bin/env python3
"""ブログ「OpenAI新機能まとめ 2026年7〜9月」の図解と作例画像を生成する（2026-09-30）。
- 図解（日本語入り）: gpt-image-2（実績のある既定。FLAT様式）
- 作例: gpt-image-2.5-sunburst / flare（9/8公開のImages 2.5系をAPIで実際に使った作例）
生成後は原寸で全日本語を目視検品する。
usage: python3 tools/gen_openai_q3_assets.py [key ...]   # 引数なしで全件。FORCE=1 で上書き
"""
import os, sys, json, time, base64, subprocess, threading
from concurrent.futures import ThreadPoolExecutor
import requests
from imagegen import KEYS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = 'openai-shinkino-matome-2026-q3'
OUT = os.path.join(ROOT, 'public', 'blog', SLUG)
RAW = os.path.join(ROOT, '..', 'WizTry-AI', 'output', 'WizTry', '2026-09-30_OpenAI新機能まとめブログ', '画像_原寸')
LOG = os.path.join(RAW, '_gen-log.jsonl')
os.makedirs(OUT, exist_ok=True)
os.makedirs(RAW, exist_ok=True)
H = {'Authorization': f"Bearer {KEYS['OPENAI_API_KEY']}"}
lock = threading.Lock()

FLAT = ("Flat vector infographic illustration, cream background (#FAF3E7), warm orange (#E1794A) as the main accent, "
        "navy (#0a1630) for text and outlines, a friendly small white robot mascot with a simple face, rounded shapes, "
        "no gradients, no glow, no 3D, no photorealism, clean generous margins, Japanese corporate blog style. "
        "All Japanese text must be rendered EXACTLY as specified, in a bold gothic (sans-serif) font, crisp and legible. "
        "Never draw the corner brackets 「」 — they only mark the text boundaries in this prompt. "
        "Do not draw any other words, numbers, logos, watermarks or pseudo-text. No real company logos or app icons. ")

# key: (model, size, prompt, [edit_source_key])
JOBS = {
  # ---------- 図解（gpt-image-2・3:2）
  'diagram-01-5henka': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: a title at the top reading exactly 「この3か月で起きた5つの変化」. Below it, five rounded cards in a single row, each with a large orange number badge, a simple icon and a short label. "
    "Card 1: badge 「1」, a brain icon, label exactly 「頭脳がGPT-6世代へ」. "
    "Card 2: badge 「2」, a robot handing over a finished document, label exactly 「答えるAIから納品するAIへ」. "
    "Card 3: badge 「3」, a picture frame with a paint brush, label exactly 「画像生成が2.5に」. "
    "Card 4: badge 「4」, a microphone with sound waves, label exactly 「声で仕事を頼める」. "
    "Card 5: badge 「5」, a calendar with a warning mark, label exactly 「終わる機能と移行期限」. "
    "Labels may wrap to two lines inside each card. The white robot mascot waves from the bottom right corner."),
  'diagram-02-chizu': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: a title at the top reading exactly 「新機能の地図（2026年7〜9月）」. Below it, a large open bookshelf with seven labeled shelves/boxes arranged in two rows (4 on top, 3 below), each box with one simple icon and a label. "
    "The seven labels EXACTLY: 「モデル（頭脳）」 with a brain icon, 「ChatGPT Work」 with a briefcase icon, 「画像生成」 with a picture icon, "
    "「音声」 with a microphone icon, 「社内ツール連携」 with a plug icon, 「料金・プラン」 with a coin icon, 「終わる機能」 with a calendar icon. "
    "The white robot mascot stands next to the shelf pointing at it."),
  'diagram-03-nenpyo': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: a horizontal timeline arrow across the middle with three big columns. Title at the top reading exactly 「3か月の年表」. "
    "Column header 「7月」 with three stacked tags below: 「GPT-5.6」, 「ChatGPT Work」, 「新しい音声モード」. "
    "Column header 「8月」 with three stacked tags below: 「無料版の文字チャット無制限」, 「Business Premium」, 「条件で動くタスク」. "
    "Column header 「9月」 with three stacked tags below: 「GPT-6 Astra」, 「Images 2.5」, 「dots（常駐AI）」. "
    "The column headers are large orange circles with white text. The white robot mascot walks along the arrow at the right end."),
  'diagram-04-model': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「どの仕事に、どの頭脳？」. Below it, four horizontal rows, each row is a rounded pill on the left with a model name and an arrow pointing right to a description box. "
    "Row 1: left 「GPT-6 Astra」, right 「ここ一番の資料・難しい作業」. "
    "Row 2: left 「GPT-6.1 Sol」, right 「迷ったらこれ。日常の主力」. "
    "Row 3: left 「GPT-6 Luna」, right 「仕分け・要約を大量に」. "
    "Row 4: left 「GPT-5.6（Chat画面）」, right 「ふだんの相談・文章直し」. "
    "Use a small icon at the far right of each row: a trophy, a star, a stack of papers, a speech bubble. The white robot mascot peeks from the bottom left."),
  'diagram-05-hatarakikata': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「ChatGPTの3つの働き方」. Below it, three tall cards side by side, each with a scene illustration of the white robot and a label and a small caption. "
    "Card 1: the robot sitting across a desk answering a person's question with a speech bubble, header exactly 「Chat」, caption exactly 「その場で答える相談相手」. "
    "Card 2: the robot handing a finished report and a slide deck to a person, header exactly 「Work」, caption exactly 「任せると納品する部下」. "
    "Card 3: the robot sitting at its own small computer at night under a moon, watching an inbox, header exactly 「dots」, caption exactly 「ずっと見張る番頭さん」. "
    "Under the cards, a thin orange arrow from left to right with the text exactly 「任せる範囲が広がる」."),
  'diagram-06-work': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「Workにできることが増えた」. Below it, a 2x2 grid of rounded cards, each with an icon and a label. "
    "Card 1: an envelope with a lightning bolt, label exactly 「メールが届いたら自動で動く」. "
    "Card 2: a browser window with a key and a padlock, label exactly 「ログインが必要なサイトでも作業」. "
    "Card 3: a small web page with a share arrow, label exactly 「社内向けページを作って共有」. "
    "Card 4: a bar chart connected to a database cylinder, label exactly 「データをつないで分析」. "
    "The white robot mascot sits in the center of the grid holding a checklist."),
  'diagram-07-prompt': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「画像の頼み方 5つの順番」. Below it, five rounded blocks connected by orange arrows from left to right like a recipe, each with a number badge, an icon and a label. "
    "Block 1: 「1」, a target icon, 「用途」. Block 2: 「2」, a gift box icon, 「主役」. Block 3: 「3」, a camera frame icon, 「構図」. "
    "Block 4: 「4」, a palette icon, 「雰囲気」. Block 5: 「5」, a shield icon, 「守ること」. "
    "Under the arrows, one wide bar with the text exactly 「入れたい文字は一字一句そのまま書く」. "
    "The white robot mascot holds a paintbrush at the bottom right."),
  'diagram-08-images25': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「Images 2.5の新しい道具」. Below it, four cards in a row, each with a scene and a label. "
    "Card 1: a grid of poster and flyer templates, label exactly 「テンプレート」. "
    "Card 2: a rough pencil sketch turning into a finished colorful picture with an arrow, label exactly 「ラフ画から清書」. "
    "Card 3: a picture with a small comment pin on one spot, label exactly 「直したい所にコメント」. "
    "Card 4: a note card being passed between two hands, label exactly 「頼み方を共有」. "
    "The white robot mascot holds a camera at the bottom left."),
  'diagram-09-onsei': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「声でAIに仕事を頼む」. On the left, a person wearing a hard hat talking into a smartphone while the white robot on the phone screen listens, with sound waves in both directions. "
    "On the right, four stacked rounded label boxes each with a small icon: 「聞きながら話せる」 (two overlapping speech bubbles), 「資料を見せて質問」 (a document), "
    "「声でWorkを動かす」 (a briefcase), 「会議メモを自動で残す」 (a notepad)."),
  'diagram-10-renkei': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「いつもの道具の中にChatGPT」. In the center, a circle with the white robot mascot. Around it, six rounded boxes connected by orange lines, each a generic icon (no real logos) with a label: "
    "「Word」 (a generic document page icon), 「PowerPoint」 (a generic slide icon), 「Google ドライブ」 (a generic folder icon), "
    "「Slack・Teams」 (a generic chat bubbles icon), 「Gmail・カレンダー」 (a generic envelope and calendar icon), 「Box・SharePoint」 (a generic cloud box icon). "
    "Do not draw any real product logos, only the plain text labels."),
  'diagram-11-plan': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「会社で使うプランの選び方」. Below it, four ascending stair steps from bottom left to top right, the white robot climbing them, each step with a label: "
    "Step 1 (lowest): 「無料・Goで試す」. Step 2: 「Plusで仕事を任せる」. Step 3: 「Businessで会社のルール」. Step 4 (highest): 「よく使う人だけPremium」. "
    "Each step has a small icon: a sprout, a briefcase, a building, a star."),
  'diagram-12-kigen': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「終わる機能・移行のカレンダー」. Left two thirds: three large calendar pages in a row, each with a date header in orange and a label below: "
    "「10/14」 with label 「GPT-5.5が終了」, 「11/30」 with label 「Agent Builderが停止」, 「12/11」 with label 「カスタムGPTが廃止」 (this third page is highlighted with a thick orange border). "
    "Right third: a box with header exactly 「すでに終了」 and three lines: 「Atlasブラウザ」, 「Soraアプリ」, 「グループチャットの新規作成」. "
    "The white robot mascot holds an alarm clock at the bottom."),
  'diagram-13-3step': ('gpt-image-2', '1536x1024', FLAT +
    "Layout: title at the top reading exactly 「明日からの3ステップ」. Below it, three large rounded cards connected by orange arrows from left to right, each with a big number and an icon and a label. "
    "Card 1: 「1」, a clipboard with a checklist, label exactly 「社内のGPTsを棚卸し」. "
    "Card 2: 「2」, a briefcase, label exactly 「Workに仕事を1つ任せる」. "
    "Card 3: 「3」, a picture and a microphone, label exactly 「画像と音声を1回ずつ試す」. "
    "The white robot mascot gives a thumbs up at the bottom right."),
  # ---------- 作例（Images 2.5 系・API）
  'sakurei-01-chirashi-sunburst': ('gpt-image-2.5-sunburst', '1024x1536',
    "A4 portrait flyer for a small family-run Japanese diner's autumn set-meal fair. Warm, appetizing, hand-crafted feel. "
    "Main visual: a beautifully plated Japanese set meal with chestnut rice (kuri gohan), grilled salmon, miso soup and pickles on a wooden tray, soft autumn window light, a few maple leaves. "
    "Text (render exactly, Japanese, no other text anywhere): top headline large brush-style 「秋の定食フェア」; under it 「10月1日〜31日」; near the food 「栗ごはん定食」; bottom small 「まるやま食堂」. "
    "Layout: headline at top, photo in the middle, shop name at bottom center, generous margins, cream and deep red color scheme. No logos, no QR codes, no prices."),
  'sakurei-01-chirashi-flare': ('gpt-image-2.5-flare', '1024x1536',
    "A4 portrait flyer for a small family-run Japanese diner's autumn set-meal fair. Warm, appetizing, hand-crafted feel. "
    "Main visual: a beautifully plated Japanese set meal with chestnut rice (kuri gohan), grilled salmon, miso soup and pickles on a wooden tray, soft autumn window light, a few maple leaves. "
    "Text (render exactly, Japanese, no other text anywhere): top headline large brush-style 「秋の定食フェア」; under it 「10月1日〜31日」; near the food 「栗ごはん定食」; bottom small 「まるやま食堂」. "
    "Layout: headline at top, photo in the middle, shop name at bottom center, generous margins, cream and deep red color scheme. No logos, no QR codes, no prices."),
  'sakurei-02-shohin-before': ('gpt-image-2.5-sunburst', '1024x1024',
    "Product photo for an online shop: a single glass jar of amber honey with a plain kraft-paper label that reads exactly 「阿蘇のはちみつ」 in simple black Japanese gothic letters, "
    "a wooden honey dipper beside it, pure white seamless background, soft even studio lighting, sharp focus, e-commerce catalog style. No other text, no logos."),
  'sakurei-02-shohin-after': ('gpt-image-2.5-sunburst', '1024x1024',
    "Edit this product photo. Change ONLY the background and lighting: place the jar on a rustic wooden table outdoors with a softly blurred green grassland and distant mountains, warm late-afternoon sunlight. "
    "Keep the jar, its shape, the honey color, the label and its text 「阿蘇のはちみつ」, and the wooden dipper exactly the same. Do not add any other text or logos.", 'sakurei-02-shohin-before'),
  'sakurei-03-kyujin': ('gpt-image-2.5-sunburst', '1024x1536',
    "Recruitment poster for a small local construction and electrical-work company in Japan. Friendly, trustworthy, modern flat illustration style. "
    "Illustration: three smiling workers of different ages (one woman, two men) in clean work uniforms and helmets standing in front of a newly built house, blue sky. "
    "Text (render exactly, Japanese, no other text anywhere): big headline at top 「現場スタッフ募集」; below 「未経験から、手に職を。」; bottom band 「見学・相談だけでも歓迎」. "
    "Navy and bright yellow color scheme, generous margins. No logos, no phone numbers, no salaries."),
  'sakurei-04-stamp': ('gpt-image-2.5-sunburst', '1024x1024',
    "A sticker pack sheet: four die-cut stickers arranged in a 2x2 grid on a plain white background, featuring the same original mascot character in every sticker: "
    "a round, cheerful orange tabby cat wearing a small navy work apron. Consistent character design across all four. Thick white sticker outline, flat colors, cute Japanese style. "
    "Each sticker has one short Japanese phrase, render exactly: top-left 「ありがとう！」 (cat bowing happily), top-right 「了解です」 (cat saluting), "
    "bottom-left 「おつかれさま」 (cat holding a cup of tea), bottom-right 「よろしくお願いします」 (cat bowing politely). No other text, no logos, not any existing famous character."),
  'sakurei-05-sketch': ('gpt-image-2', '1536x1024',
    "A rough hand-drawn pencil sketch on white paper of a Japanese living room renovation plan, drawn quickly by an amateur: simple lines showing a low sofa, a wooden dining table, "
    "a large window on the left, tatami corner on the right, a pendant light, some notes drawn as scribbles without readable words. Black pencil only, loose uneven lines, no color, no text."),
  'sakurei-05-kansei': ('gpt-image-2.5-sunburst', '1536x1024',
    "Turn this rough pencil sketch into a finished photorealistic interior rendering. Keep the same layout and positions exactly: low sofa, wooden dining table, large window on the left, "
    "raised tatami corner on the right, pendant light. Style: warm Japanese modern (wa-modern), light oak wood, white plaster walls, soft natural daylight, a few green plants. No text, no people.", 'sakurei-05-sketch'),
}


def log(rec):
    with lock:
        with open(LOG, 'a') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')


def run(key):
    model, size, prompt, *src = JOBS[key]
    png = os.path.join(RAW, key + '.png')
    if os.path.exists(png) and not os.environ.get('FORCE'):
        return f'skip {key}'
    t0 = time.time()
    for attempt in range(3):
        try:
            if src:
                with open(os.path.join(RAW, src[0] + '.png'), 'rb') as f:
                    r = requests.post('https://api.openai.com/v1/images/edits', headers=H, timeout=600,
                                      files={'image[]': (src[0] + '.png', f, 'image/png')},
                                      data={'model': model, 'prompt': prompt, 'size': size, 'quality': 'high'})
            else:
                r = requests.post('https://api.openai.com/v1/images/generations', headers=H, timeout=600,
                                  json={'model': model, 'prompt': prompt, 'size': size, 'quality': 'high', 'n': 1})
            r.raise_for_status()
            d = r.json()
            open(png, 'wb').write(base64.b64decode(d['data'][0]['b64_json']))
            sec = round(time.time() - t0, 1)
            log({'key': key, 'model': model, 'size': size, 'sec': sec, 'usage': d.get('usage')})
            width = '1400' if size == '1536x1024' else ('900' if size == '1024x1536' else '1000')
            subprocess.run(['cwebp', '-quiet', '-q', '84', '-resize', width, '0', png,
                            '-o', os.path.join(OUT, key + '.webp')], check=True)
            return f'OK {key} {model} {sec}s'
        except Exception as e:
            err = str(e)[:200]
            try:
                err += ' ' + r.text[:300]
            except Exception:
                pass
            if attempt == 2:
                return f'FAIL {key}: {err}'
            time.sleep(5)


def main():
    keys = sys.argv[1:] or list(JOBS)
    first = [k for k in keys if len(JOBS[k]) == 3]
    second = [k for k in keys if len(JOBS[k]) == 4]
    with ThreadPoolExecutor(4) as ex:
        for msg in ex.map(run, first):
            print(msg, flush=True)
    with ThreadPoolExecutor(2) as ex:
        for msg in ex.map(run, second):
            print(msg, flush=True)


if __name__ == '__main__':
    main()
