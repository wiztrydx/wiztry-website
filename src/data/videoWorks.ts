// AI動画制作（/ai-video/）のポートフォリオ。
// 【公開リポジトリ】このファイルは誰でも読める。取引先の社名・商品名・社内事情は書かない（業種名まで）。
// 作品ごとの制作者・掲載許可の根拠は、社内の資料室（WizTry-AI）の
// output/WizTry/2026-10-12_AI動画制作サービスページ/README.md に書く。slug も中立な名前にする。
//
// 【掲載許可のゲート】permission が 'cleared' の作品だけが本番ビルドに出る。
// 'pending' の作品は開発サーバー（npm run dev）でだけ「掲載確認待ち」の印つきで表示され、
// 動画ファイルは public/videos/works-pending/（.gitignore でフォルダごと除外）に置く。
// 許可が取れたら permission を 'cleared' にし、mp4 と webp を public/videos/works/ へ移してコミットする。
// 配備は GitHub Actions（git の中身からビルド）だけにする。ローカルの dist/ を直接アップロードすると
// public/ を丸ごとコピーした確認待ちの動画まで出てしまう。
//
// 動画の変換・ポスター・ヒーロー背景のダイジェストは tools/prep_video_works.py と tools/video_works.json。
export type VideoCategory = '企業PVとCM' | '商品PR' | 'SNSショート' | '解説動画とアバター' | 'オリジナル曲とMV';

export type VideoWork = {
  /** 動画ファイル名（拡張子なし）。社名・商品名を入れない */
  slug: string;
  /** カードの1行目。「何の動画か」が分かる名前 */
  title: string;
  /** 発注元（業種名まで）。自社制作は「WizTry（自社）」 */
  client: string;
  category: VideoCategory;
  orientation: 'landscape' | 'portrait';
  /** 表示用の長さ（例 '1:30'） */
  duration: string;
  /** 構造化データ用の長さ（ISO 8601。例 'PT1M30S'） */
  durationIso: string;
  /** 構造化データ用の納品・公開日（YYYY-MM-DD） */
  date: string;
  /** どう作ったか（カードの2行目） */
  method: string;
  /** 先方の掲載許可。'cleared' だけが本番に出る。根拠は資料室の README（このファイルには書かない） */
  permission: 'cleared' | 'pending';
};

export const VIDEO_WORKS: VideoWork[] = [
  {
    slug: 'association-pv',
    title: 'お金の専門家の役割を伝えるPV',
    client: '業界団体 様',
    category: '企業PVとCM',
    orientation: 'landscape',
    duration: '2:49',
    durationIso: 'PT2M49S',
    date: '2026-10-12',
    method: 'AIで生成したアニメーションで、撮影なしで制作',
    permission: 'pending',
  },
  {
    slug: 'exhibition-brand',
    title: '展示会ブースで流すブランド映像',
    client: '半導体メーカー 様（台湾）',
    category: '企業PVとCM',
    orientation: 'landscape',
    duration: '1:06',
    durationIso: 'PT1M6S',
    date: '2026-06-02',
    method: '製品カタログだけを預かり、撮影なしで制作。日本語と英語、繁体字中国語の3言語版を納品',
    permission: 'pending',
  },
  {
    slug: 'image-song-ad',
    title: 'イメージソングのYouTube広告',
    client: '住宅リフォーム会社 様',
    category: 'オリジナル曲とMV',
    orientation: 'landscape',
    duration: '0:30',
    durationIso: 'PT30S',
    date: '2026-07-23',
    method: 'イメージソングに合わせて、AIで生成した映像と施工写真を組み合わせて制作',
    permission: 'pending',
  },
  {
    slug: 'app-intro',
    title: 'AIアプリの紹介動画',
    client: '住宅リフォーム会社 様',
    category: '商品PR',
    orientation: 'landscape',
    duration: '0:30',
    durationIso: 'PT30S',
    date: '2026-09-29',
    method: 'AIで生成した映像に、アプリの実際の画面と写真を組み合わせて制作',
    permission: 'pending',
  },
  {
    slug: 'necklace-ad-1',
    title: 'パールネックレスの広告動画「自信・印象アップ編」',
    client: '宝飾品の販売会社 様',
    category: 'SNSショート',
    orientation: 'portrait',
    duration: '0:34',
    durationIso: 'PT34S',
    date: '2026-09-17',
    method: '商品写真をもとに、AIでSNS向けの縦型動画に',
    permission: 'cleared',
  },
  {
    slug: 'necklace-ad-2',
    title: 'パールネックレスの広告動画「冠婚葬祭から日常へ編」',
    client: '宝飾品の販売会社 様',
    category: 'SNSショート',
    orientation: 'portrait',
    duration: '0:38',
    durationIso: 'PT38S',
    date: '2026-09-17',
    method: '商品写真をもとに、AIでSNS向けの縦型動画に',
    permission: 'cleared',
  },
  {
    slug: 'necklace-ad-3',
    title: 'パールネックレスの広告動画「安心して選べる編」',
    client: '宝飾品の販売会社 様',
    category: 'SNSショート',
    orientation: 'portrait',
    duration: '0:40',
    durationIso: 'PT40S',
    date: '2026-09-17',
    method: '商品写真をもとに、AIでSNS向けの縦型動画に',
    permission: 'cleared',
  },
  {
    slug: 'crystal-ad',
    title: '天然水晶の置物の広告動画',
    client: '宝飾品の販売会社 様',
    category: '商品PR',
    orientation: 'portrait',
    duration: '0:35',
    durationIso: 'PT35S',
    date: '2026-05-12',
    method: 'AIで生成した映像で、縦型の広告動画に',
    permission: 'cleared',
  },
];

/** 画面に出す作品。本番は掲載許可済み（cleared）だけ、開発サーバーでは確認待ちも出す */
export const visibleVideoWorks = (): VideoWork[] =>
  import.meta.env.DEV ? VIDEO_WORKS : VIDEO_WORKS.filter((w) => w.permission === 'cleared');

/** 動画とポスターの置き場所。確認待ちは公開リポジトリに入らない works-pending/ */
export const videoFile = (w: VideoWork, ext: 'mp4' | 'webp'): string =>
  `/videos/${w.permission === 'cleared' ? 'works' : 'works-pending'}/${w.slug}.${ext}`;

export const VIDEO_CATEGORIES: VideoCategory[] = ['企業PVとCM', '商品PR', 'SNSショート', '解説動画とアバター', 'オリジナル曲とMV'];
