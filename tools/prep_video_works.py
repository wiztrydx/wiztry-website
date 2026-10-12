#!/usr/bin/env python3
"""AI動画制作ページ（/ai-video/）の作品動画をサイト用に変換する（2026-10-12）。

1. 作品ごとに 720p の H.264 MP4（+faststart）と、ポスター画像（WebP）を作る
   掲載許可済み（src/data/videoWorks.ts で permission: 'cleared'）→ public/videos/works/<slug>.mp4 / .webp
   確認待ち（'pending'）→ public/videos/works-pending/（.gitignore でフォルダごと除外。公開リポジトリに入れない）
2. reel_order の作品の抜粋をつないだ無音のダイジェストをヒーロー背景用に作る
   → public/videos/ai-video/showreel-pc.mp4（1280x720）/ showreel-sp.mp4（540x960）
   本番に出るので、reel_order には掲載許可済みの作品だけを入れる（確認待ちが混ざると止める）。

設定は tools/video_works.json（秒数など。公開してよい情報だけ）。元動画の場所は手元だけの JSON で渡す:
  {"<slug>": "/path/to/source.mp4", ...}
usage: python3 tools/prep_video_works.py <src_map.json> [slug ...]   # slug 指定なしで全作品＋ダイジェスト
元ファイルは読むだけで、変更しない。
"""
import json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEOS = os.path.join(ROOT, 'public', 'videos')
REEL = os.path.join(VIDEOS, 'ai-video')
CONFIG = os.path.join(ROOT, 'tools', 'video_works.json')
DATA_TS = os.path.join(ROOT, 'src', 'data', 'videoWorks.ts')


def permissions():
    """videoWorks.ts から slug ごとの掲載許可を読む（正本はTS側。ここで二重管理しない）"""
    ts = open(DATA_TS, encoding='utf-8').read()
    pairs = re.findall(r"slug: '([^']+)'.*?permission: '(cleared|pending)'", ts, flags=re.S)
    return dict(pairs)


def sh(*args):
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def has_audio(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type', '-of', 'json', path],
                         check=True, capture_output=True, text=True).stdout
    return any(s.get('codec_type') == 'audio' for s in json.loads(out).get('streams', []))


def encode_work(w, src, cleared):
    out_dir = os.path.join(VIDEOS, 'works' if cleared else 'works-pending')
    os.makedirs(out_dir, exist_ok=True)
    slug = w['slug']
    portrait = w.get('orientation') == 'portrait'
    scale = 'scale=-2:min(1280\\,ih)' if portrait else 'scale=min(1280\\,iw):-2'
    dst = os.path.join(out_dir, f'{slug}.mp4')
    args = ['ffmpeg', '-y', '-i', src, '-vf', f'{scale},fps=fps=min(30\\,source_fps),format=yuv420p',
            '-c:v', 'libx264', '-preset', 'slow', '-crf', str(w.get('crf', 25)), '-profile:v', 'high',
            '-maxrate', '3M', '-bufsize', '6M', '-movflags', '+faststart']
    args += ['-c:a', 'aac', '-b:a', '128k', '-ac', '2'] if has_audio(src) else ['-an']
    sh(*args, dst)
    # ポスター: 指定秒のフレーム（字幕の少ない場面を選ぶ）
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        png = f.name
    sh('ffmpeg', '-y', '-ss', str(w.get('poster_at', 3.0)), '-i', src, '-frames:v', '1', png)
    sh('cwebp', '-quiet', '-q', '80', '-resize', '540' if portrait else '960', '0', png,
       '-o', os.path.join(out_dir, f'{slug}.webp'))
    os.unlink(png)
    return dst


def build_reel(cfg, srcs, perm):
    order = cfg['reel_order']
    leaked = [s for s in order if perm.get(s) != 'cleared']
    if leaked:
        sys.exit(f'reel_order に掲載許可済みでない作品があります: {leaked}')
    os.makedirs(REEL, exist_ok=True)
    by_slug = {w['slug']: w for w in cfg['works']}
    for name, (W, H) in {'showreel-pc': (1280, 720), 'showreel-sp': (540, 960)}.items():
        inputs, chains = [], []
        for i, slug in enumerate(order):
            w = by_slug[slug]
            inputs += ['-ss', str(w.get('reel_at', 5.0)), '-t', str(w.get('reel_len', 4.0)), '-i', srcs[slug]]
            fill = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}'
            if w.get('orientation') == 'portrait' and W > H:
                # 横長の画面に縦型の作品を置くときは、ぼかした同じ映像を背景に敷き、文字の載らない右側に置く
                chains.append(
                    f'[{i}:v]split[a{i}][b{i}];'
                    f'[a{i}]{fill},boxblur=20:2,eq=brightness=-0.15[bg{i}];'
                    f'[b{i}]scale=-2:{H}[fg{i}];'
                    f'[bg{i}][fg{i}]overlay=x=W*0.7-w/2:y=0,fps=30,format=yuv420p,setsar=1[v{i}]')
            else:
                chains.append(f'[{i}:v]{fill},fps=30,format=yuv420p,setsar=1[v{i}]')
        concat = ''.join(f'[v{i}]' for i in range(len(order))) + f'concat=n={len(order)}:v=1:a=0[out]'
        dst = os.path.join(REEL, f'{name}.mp4')
        sh('ffmpeg', '-y', *inputs, '-filter_complex', ';'.join(chains + [concat]), '-map', '[out]', '-an',
           '-c:v', 'libx264', '-preset', 'slow', '-crf', '30', '-profile:v', 'high', '-movflags', '+faststart', dst)
        print('reel', dst, os.path.getsize(dst) // 1024, 'KB', flush=True)


if __name__ == '__main__':
    srcs = json.load(open(sys.argv[1]))
    only = set(sys.argv[2:])
    cfg = json.load(open(CONFIG))
    perm = permissions()
    for w in cfg['works']:
        if only and w['slug'] not in only:
            continue
        dst = encode_work(w, srcs[w['slug']], perm.get(w['slug']) == 'cleared')
        print('work', dst, os.path.getsize(dst) // 1024, 'KB', flush=True)
    if not only:
        build_reel(cfg, srcs, perm)
