#!/usr/bin/env python3
"""実績ページ・応援ナビ／FMK記事用の図解・ヒーロー画像を生成する（2026-09-17）。
日本語文字入りは gpt-image-2 固定（imagegen.py の優先順位どおり）。生成後は原寸で全文字を目視検品する。
usage: python3 tools/gen_navi_assets.py [key ...]   # 引数なしで全件。FORCE=1 で上書き
"""
import os, sys, subprocess
from imagegen import generate

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, 'public')

FLAT = ("Flat vector infographic illustration, cream background (#FAF3E7), warm orange (#E1794A) as the main accent, "
        "navy (#0a1630) for text and outlines, a friendly small white robot mascot with a simple face, rounded shapes, "
        "no gradients, no glow, no 3D, no photorealism, clean generous margins, Japanese corporate blog style. "
        "All Japanese text must be rendered EXACTLY as specified, in a bold gothic (sans-serif) font, crisp and legible. "
        "Never draw the corner brackets 「」 — they only mark the text boundaries in this prompt. "
        "Do not draw any other words, numbers, logos, watermarks or pseudo-text. ")

JOBS = {
  # --- ページのヒーロー（文字なし・16:9）
  'gen/ph-media.webp': ('16:9', 1600,
    "Premium abstract hero background for a Japanese AI company's 'media coverage' page: deep navy blue (#0a1630) gradient, "
    "softly glowing translucent icons of a TV screen, a studio microphone with radio waves, a folded newspaper and a speaker podium "
    "arranged loosely on the right side, electric blue (#2f6bff) and cyan (#37c8f0) light accents, floating light particles, "
    "cinematic lighting, clean modern web design, no text, no letters, no logos."),
  'gen/ph-projects.webp': ('16:9', 1600,
    "Premium abstract hero background for a Japanese AI company's 'projects' page: deep navy blue (#0a1630) gradient, "
    "a softly glowing translucent map of Kumamoto prefecture in Japan with several luminous location pins and a small smartphone outline "
    "on the right side, electric blue (#2f6bff) and cyan (#37c8f0) light accents, floating light particles, cinematic lighting, "
    "clean modern web design, no text, no letters, no logos."),
  # --- 図解（日本語入り・3:2）
  'blog/kumamoto-ouen-navi/diagram-1-6verbs.webp': ('3:2', 1400, FLAT +
    "Layout: a title at the top reading exactly 「きょうできる応援は、6つの入口から」. Below it, six rounded tiles in a 3x2 grid, "
    "each with a simple orange line icon and one Japanese label under it. The six labels, EXACTLY: "
    "「行く」 with a suitcase icon, 「買う」 with a shopping bag icon, 「贈る」 with a gift box icon, "
    "「作る」 with a wrench icon, 「広める」 with a megaphone icon, 「手伝う」 with two hands icon. "
    "Under the grid, one arrow pointing down to a single ledger book labelled exactly 「ひとつの応援の台帳」. "
    "The white robot mascot stands at the bottom right holding a magnifying glass."),
  'blog/kumamoto-ouen-navi/diagram-2-3yakusoku.webp': ('3:2', 1400, FLAT +
    "Layout: a title at the top reading exactly 「掲載の3つの約束」. Below it, three vertical cards side by side, each with a large orange number badge and an icon and a short label. "
    "Card 1: badge 「1」, an icon of a coin with a red prohibition slash, label exactly 「お金を扱わない」. "
    "Card 2: badge 「2」, an icon of a document with a link and a clock, label exactly 「全件に出典と確認時刻」. "
    "Card 3: badge 「3」, an icon of a robot handing a paper to a person who holds a checkmark stamp, label exactly 「AIが集め、人が確かめてから出す」. "
    "The white robot mascot peeks from the bottom left corner."),
  'projects/diagram-2chapters.webp': ('3:2', 1400, FLAT +
    "Layout: two large rounded panels side by side connected by a double-headed arrow in the middle. "
    "Left panel header exactly 「第1章 くまもと被災者支援ナビ」 with a subtitle exactly 「支援を受ける側へ」, "
    "an icon of a water tap and a house, and a small phone showing a map with pins. "
    "Right panel header exactly 「第2章 くまもと応援ナビ」 with a subtitle exactly 「応援する側へ」, "
    "an icon of a suitcase and a gift box, and a small phone showing a list. "
    "Above both panels, a single title reading exactly 「地震の翌日から、ふたつのナビ」. "
    "At the very bottom, a wide orange bar with white text exactly 「AIが集め、人が確かめ、出典つきで届ける」. "
    "The white robot mascot stands between the two panels."),
  'blog/fmk-instyle-shien-navi/diagram-1-koteki-dosen.webp': ('3:2', 1400, FLAT +
    "Layout: in the center, a smartphone showing a simple map with pins, captioned below exactly 「くまもと被災者支援ナビ」. "
    "Around it, five rounded label boxes each connected to the phone by an orange arrow pointing toward the phone. "
    "The five box labels, EXACTLY: 「熊本県 公式サイト・LINE」, 「八代市 公式サイト・LINE・X」, 「防災科研 防災クロスビュー」, "
    "「テレビ熊本 生活情報ページ」, 「熊本県国際協会」. "
    "Title at the top reading exactly 「公的機関・メディアからの導線」. Keep every label on a single line. The white robot mascot sits at the bottom right."),
  'blog/fmk-instyle-shien-navi/radio-live.webp': ('3:2', 1400,
    "Warm flat vector illustration, cream background (#FAF3E7), orange (#E1794A) accents, navy outlines: a friendly small white robot with a simple face "
    "sits at a desk wearing headphones in front of a large studio microphone, a laptop shows a video-call window with a person, "
    "soft radio wave arcs spread from the microphone toward a small radio on the right, a smartphone on the desk shows a map with pins. "
    "No text, no letters, no logos, no numbers anywhere. No gradients, no glow, no 3D."),
  'blog/kumamoto-ouen-navi-hanbai-kaishi/diagram-1-living-renkei.webp': ('3:2', 1400, FLAT +
    "Layout: two rounded panels side by side with two curved orange arrows between them forming a loop (mutual introduction). "
    "Left panel: an icon of a folded newspaper and a smartphone app icon, header exactly 「リビング熊本（紙面・アプリ）」, "
    "a small line under it exactly 「応援ナビを紹介」. "
    "Right panel: an icon of a smartphone showing a map of Kumamoto with pins, header exactly 「くまもと応援ナビ」, "
    "a small line under it exactly 「アプリのダウンロード先を案内」. "
    "Title at the top reading exactly 「連携メディアとして、お互いに案内し合う」. "
    "At the bottom, a small note in navy exactly 「お金のやり取りはありません」. The white robot mascot stands in the middle below the arrows."),
}

def to_webp(png_path, out_path, width):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    subprocess.run(['cwebp', '-quiet', '-q', '84', '-resize', str(width), '0', png_path, '-o', out_path], check=True)

def main():
    targets = sys.argv[1:]
    for rel, (aspect, width, prompt) in JOBS.items():
        if targets and not any(t in rel for t in targets):
            continue
        out = os.path.join(PUB, rel)
        if os.path.exists(out) and not os.environ.get('FORCE'):
            print('skip', rel); continue
        try:
            raw, model = generate(prompt, aspect)
            tmp = out + '.tmp.png'
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(tmp, 'wb').write(raw)
            to_webp(tmp, out, width)
            os.rename(tmp, out.replace('.webp', '.src.png'))
            print('OK', rel, model)
        except Exception as e:
            print('FAIL', rel, str(e)[:200])

if __name__ == '__main__':
    main()
