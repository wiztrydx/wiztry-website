#!/usr/bin/env python3
"""事業内容の4本柱化（HP制作・AI動画制作の追加）と /ai-video/ ページ用の画像を生成する（2026-10-12）。
既存の scene-*.webp（明るいオフィスの実写風）と ph-*.webp（濃紺の抽象背景）に様式を合わせる。
アイコンは絵文字を使わない方針（HP系の品質基準）のため、同一プレフィックスで連作する。
usage: python3 tools/gen_service_assets.py [key ...]   # 引数なしで全件。FORCE=1 で上書き
"""
import os, sys, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor
from imagegen import generate

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'public', 'gen')

PHOTO = ("Photorealistic corporate photograph, bright modern Japanese office with large windows and soft natural daylight, "
         "warm wood and white interior, shallow depth of field, clean and trustworthy mood, subtle navy and blue accents, "
         "shot on a full-frame camera, 35mm lens. No text, no letters, no logos, no watermarks, no brand names on screens. ")

ABSTRACT = ("Abstract dark navy background (#050d1e to #163464), elegant glowing light in electric blue (#2f6bff) and cyan (#37c8f0), "
            "fine particles, cinematic depth, premium technology brand key visual. The left 45% of the frame stays dark and calm "
            "so white headline text can sit on it; the visual interest is on the right side. No text, no letters, no logos. ")

ICON = ("A single 3D icon, soft glossy glass and frosted acrylic material, navy (#0a1630) and electric blue (#2f6bff) with cyan (#37c8f0) highlights, "
        "gentle studio lighting, centered with generous margin, isolated on a pure white (#ffffff) background with a very soft contact shadow, "
        "consistent premium app-icon style. No text, no letters, no numbers. ")

# key: (aspect, prompt, cwebp resize width)
JOBS = {
    'scene-web-dev': ('3:2', PHOTO +
        "A Japanese web designer in a smart casual shirt works at a desk, seen from a three-quarter angle. A large monitor shows a clean, modern corporate "
        "website layout with a big hero photo and neat cards (abstract shapes only, no readable text), and a smartphone on a stand next to it shows the "
        "same site in a mobile layout. A notebook with wireframe sketches lies on the desk.", 1400),
    'scene-ai-video': ('3:2', PHOTO +
        "A Japanese video editor wearing headphones around the neck works at a desk with two monitors. The main monitor shows a video editing timeline with "
        "colorful clips and audio waveforms, and the preview window shows a cinematic, beautifully lit product shot of a pearl necklace. "
        "There is no camera, no tripod, no lighting equipment and no film crew anywhere; the scene clearly shows video being created on the computer.", 1400),
    'ph-ai-video': ('16:9', ABSTRACT +
        "On the right side, a flowing ribbon of translucent film frames and video thumbnails made of light curves through space like a filmstrip, "
        "with a soft glowing play-button shape formed by light at its center.", 1920),
    'icon-no-camera': ('1:1', ICON + "A video camera with a clean diagonal line crossing it out, meaning 'no filming needed'.", 360),
    'icon-fast': ('1:1', ICON + "A desk calendar page with a small lightning bolt beside it, meaning 'fast delivery'.", 360),
    'icon-cost': ('1:1', ICON + "A price tag (a rectangular label shape with a round hole and a short string, blank face with no symbols) with a small downward arrow beside it, meaning 'lower cost'.", 360),
    'icon-quality': ('1:1', ICON + "A faceted diamond gem with a small sparkle, meaning 'high quality'.", 360),
}


def run(key):
    dst = os.path.join(OUT, f'{key}.webp')
    if os.path.exists(dst) and not os.environ.get('FORCE'):
        return f'skip {key}'
    aspect, prompt, width = JOBS[key]
    data, label = generate(prompt, aspect)
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        f.write(data)
        src = f.name
    subprocess.run(['cwebp', '-quiet', '-q', '82', '-resize', str(width), '0', src, '-o', dst], check=True)
    os.unlink(src)
    return f'ok {key} ({label})'


if __name__ == '__main__':
    keys = sys.argv[1:] or list(JOBS)
    with ThreadPoolExecutor(max_workers=4) as ex:
        for msg in ex.map(run, keys):
            print(msg, flush=True)
