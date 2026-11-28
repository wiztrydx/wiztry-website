#!/usr/bin/env python3
"""トップページの「こんなお悩みはありませんか」用のアイコンを生成する（2026-11-28）。
様式は tools/gen_service_assets.py の ICON と同じ（紺と青のガラス質・白地）。絵文字は使わない方針のための連作。
試作は low。品質を上げるのは本人が「いい」と言った案だけ: QUALITY=high で上書きできる。
usage: python3 tools/gen_home_assets.py [key ...]   # 引数なしで全件。FORCE=1 で上書き
"""
import os, sys, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor
from imagegen import generate
from gen_service_assets import ICON

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'public', 'gen')
QUALITY = os.environ.get('QUALITY', 'low')

# key: (aspect, prompt, cwebp resize width)
JOBS = {
    'icon-worry-team': ('1:1', ICON +
        "Three simple abstract person figures side by side (rounded head and shoulders, no faces). The one on the left glows bright electric blue, "
        "the other two are dim, pale grey-blue and unlit, meaning 'only one person in the team is using it'. "
        "The figures stand directly on the plain white background: no tile, no card, no rounded square plate behind them.", 360),
    'icon-worry-start': ('1:1', ICON +
        "A wooden-style signpost made of glass with three blank arrow boards pointing in three different directions, and a small compass at its base, "
        "meaning 'not sure which way to start'. The boards are completely blank.", 360),
    'icon-worry-time': ('1:1', ICON +
        "An hourglass standing next to a tall, slightly leaning stack of paper documents, meaning 'routine paperwork takes too much time'. "
        "The papers are blank.", 360),
    'icon-worry-rule': ('1:1', ICON +
        "A shield with a small padlock on it, standing in front of a blank document sheet, meaning 'information security and usage rules'. "
        "The document has no writing.", 360),
}


def run(key):
    dst = os.path.join(OUT, f'{key}.webp')
    if os.path.exists(dst) and not os.environ.get('FORCE'):
        return f'skip {key}'
    aspect, prompt, width = JOBS[key]
    data, label = generate(prompt, aspect, quality=QUALITY)
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        f.write(data)
        src = f.name
    subprocess.run(['cwebp', '-quiet', '-q', '82', '-resize', str(width), '0', src, '-o', dst], check=True)
    os.unlink(src)
    return f'ok {key} ({label})'


if __name__ == '__main__':
    keys = sys.argv[1:] or list(JOBS)
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(run, keys):
            print(r)
