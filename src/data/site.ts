// サイト全体で使う共通データ。数字・社名を更新するときはこのファイルだけ直す。

export const SITE = {
  name: 'WizTry株式会社',
  nameEn: 'WizTry Inc.',
  domain: 'https://wiztrydx.com',
  email: 'info@wiztrydx.com',
  tel: '080-6414-9171',
  address: '〒860-0047 熊本県熊本市西区春日1丁目14番1号 くまもと森都心プラザ2階 XOSS POINT. Room4',
  founded: '2023年7月',
  ceo: '末松 光太郎',
  description:
    '熊本の生成AI研修・AIエージェント導入支援のWizTry株式会社。講師が伴走するハンズオン研修と、Claude Code・Codex等による実務自動化で、企業のAI活用を成果まで導きます。',
};

export const STATS = [
  { value: 90, unit: '社以上', label: '累計支援企業数', note: '※2026年7月時点' },
  { value: 4.8, unit: '', label: '研修満足度（5点満点）', note: '※受講後アンケート平均', decimals: 1 },
  { value: 100, unit: '%対面', label: 'ハンズオン形式の研修', note: '※オンライン併用も可能' },
  { value: 75, unit: '%', label: '補助金活用で負担軽減も', note: '※制度・要件により異なります' },
];

// 掲載許可取得済みのクライアントロゴ（ロゴ一覧シート由来）
// shape: ロゴの縦横比クラス（wide=横長ワードマーク / square=正方形 / mid=中間）表示サイズの最適化に使う
export const CLIENTS = [
  { slug: 'kumamoto-toyota', name: '熊本トヨタ自動車株式会社', shape: 'wide' },
  { slug: 'shirasagi-denki', name: '白鷺電気工業株式会社', shape: 'wide' },
  { slug: 'kumanichi-kokokusha', name: '株式会社熊日広告社', shape: 'wide' },
  { slug: 'libwork', name: '株式会社Lib Work', shape: 'wide' },
  { slug: 'shinsan-jutaku', name: '新産住拓株式会社', shape: 'mid' },
  { slug: 'kosugi-fudosan', name: 'コスギ不動産', shape: 'wide' },
  { slug: 'meiwa-fudosan', name: '明和不動産株式会社', shape: 'wide' },
  { slug: 'iwata', name: '株式会社岩田コーポレーション', shape: 'wide' },
  { slug: 'lontz-group', name: 'ロンツグループ', shape: 'square' },
  { slug: 'hisano', name: '株式会社ヒサノ', shape: 'wide' },
  { slug: 'yonezawa', name: '株式会社ヨネザワ', shape: 'mid' },
  { slug: 'kaneryo', name: 'カネリョウ海藻株式会社', shape: 'square' },
  { slug: 'nihon-shiki', name: '日本紙器株式会社', shape: 'square' },
  { slug: 'nanei-kaihatsu', name: '株式会社南栄開発', shape: 'wide' },
  { slug: 'aoyagi', name: '有限会社青柳', shape: 'square' },
  { slug: 'carepark', name: 'ケアパーク株式会社', shape: 'wide' },
  { slug: 'medicare-iyashi', name: 'メディケア癒しグループ', shape: 'wide' },
  { slug: 'hiko-dental', name: 'ヒコデンタルクリニック', shape: 'square' },
  { slug: 'do-project', name: '株式会社ドゥプロジェクト', shape: 'mid' },
  { slug: 'alma', name: 'ALMA株式会社', shape: 'square' },
  { slug: 'vietnam-trading', name: 'ベトナムトレーディング株式会社', shape: 'wide' },
] as const;

export const INDUSTRIES = [
  '不動産・住宅',
  '建設・電気設備',
  '製造',
  '運輸・物流',
  '新聞・メディア・広告',
  '金融・士業',
  '医療・歯科',
  '介護・福祉・保育',
  '小売・卸売',
  '食品',
  'IT・サービス',
  '自動車',
];

// お知らせ・メディア掲載・登壇のニュース一覧（トップと会社案内に表示）。
// date は出来事があった実際の日付。過去の実績も実日付で遡って載せる。日まで特定できないものは 'YYYY-MM'。
// url=外部リンク（別タブ）／href=サイト内リンク。どちらも無い項目はリンクなしの行になる。
// outlet があればチップに媒体名、なければ category が出る。表示側で日付の新しい順にソートされる。
export type NewsItem = {
  date: string;
  category: 'メディア掲載' | '登壇・セミナー' | 'お知らせ';
  title: string;
  outlet?: string;
  url?: string;
  href?: string;
};

export const NEWS: NewsItem[] = [
  {
    date: '2026-08-13',
    category: 'お知らせ',
    title: 'AI社員17体を1年間運用した実録記事をnoteで公開しました',
    url: 'https://note.com/note_wiztry/n/ncd98ad679178',
  },
  {
    date: '2026-08-07',
    category: 'お知らせ',
    title: '熊本県公式X「気になる！くまもと」で、くまもと被災者支援ナビが紹介されました',
  },
  {
    date: '2026-08-06',
    category: 'お知らせ',
    title: '「くまもと被災者支援ナビ」の利用がのべ10万回を超えました（ご利用と報道のご報告）',
    href: '/blog/kumamoto-shien-navi-100k/',
  },
  {
    date: '2026-08-05',
    category: 'メディア掲載',
    outlet: 'リビング熊本',
    title: '生活情報メディア「リビング熊本」で、くまもと被災者支援ナビをご紹介いただきました',
    href: '/blog/kumamoto-shien-navi-100k/',
  },
  {
    date: '2026-08-05',
    category: 'メディア掲載',
    outlet: 'テレビ熊本',
    title: 'テレビ熊本「英太郎のかたらんね」で、くまもと被災者支援ナビをご紹介いただきました',
    href: '/blog/kumamoto-shien-navi-100k/',
  },
  {
    date: '2026-08-04',
    category: 'メディア掲載',
    outlet: 'テレビ朝日',
    title: 'テレビ朝日の番組で、くまもと被災者支援ナビをご紹介いただきました',
    href: '/blog/kumamoto-shien-navi-100k/',
  },
  {
    date: '2026-08-03',
    category: 'お知らせ',
    title: 'くまもと被災者支援ナビが、八代市の公式サイト・公式LINE・公式Xで案内されるようになりました',
    href: '/blog/kumamoto-shien-navi-yatsushiro/',
  },
  {
    date: '2026-07-31',
    category: 'お知らせ',
    title: '熊本県国際協会の地震情報ページ（やさしい日本語対応）で、くまもと被災者支援ナビが紹介されました',
    url: 'https://www.kuma-koku.jp/page381.html',
  },
  {
    date: '2026-07-29',
    category: 'お知らせ',
    title: '熊本地震で被災された方向けのWebアプリ「くまもと被災者支援ナビ」を無償公開しました',
    href: '/blog/kumamoto-shien-navi/',
  },
  {
    date: '2026-07-17',
    category: '登壇・セミナー',
    title: '肥銀ビジネス教育主催の公開セミナー「生成AIハンズオン オンラインセミナー」に講師として登壇しました',
  },
  {
    date: '2026-07-10',
    category: 'お知らせ',
    title: '企業のAI研修・AI導入支援の累計支援企業数が90社を突破しました',
    href: '/blog/milestone-90-companies/',
  },
  {
    date: '2026-07-10',
    category: 'お知らせ',
    title: 'YouTubeチャンネル「KOTARO AI & VIDEO」の登録者が1,600人を突破しました',
    href: '/blog/youtube-1600-subscribers/',
  },
  {
    date: '2026-01-05',
    category: 'お知らせ',
    title: 'YouTubeチャンネル「KOTARO AI & VIDEO」を開設しました',
    url: 'https://www.youtube.com/@aivideo_biz',
  },
  {
    date: '2025-12-23',
    category: 'メディア掲載',
    outlet: 'Muse',
    title: '「挫折を原点に、挑戦し続けてきた先に見えた景色とは」— 代表・末松のインタビューが掲載されました',
    url: 'https://www.my-muse.jp/people/kotaro_suematsu/',
  },
  {
    date: '2025-10-02',
    category: '登壇・セミナー',
    title: 'レイメイ藤井主催「ソリューションフェア2025」（福岡国際センター）で、生成AI活用のトークセッションに登壇しました',
  },
  {
    date: '2025-10-01',
    category: 'お知らせ',
    title: 'オフィスをくまもと森都心プラザ2階「XOSS POINT.」へ移転しました',
    href: '/blog/office-xosspoint/',
  },
  {
    date: '2025-08-05',
    category: '登壇・セミナー',
    title: 'ビジネスイベント「Bridge for Innovation 2025 summer 熊本」（熊本城ホール）にパネル登壇・ブース出展しました',
  },
  {
    date: '2025-08-01',
    category: '登壇・セミナー',
    title: '肥後銀行ニューリーダー会のセミナーに、生成AI活用の講師として登壇しました',
  },
  {
    date: '2025-07-23',
    category: '登壇・セミナー',
    title: '熊本商工会議所・熊本県弁護士会との提携セミナーで、生成AI活用の講師を務めました',
  },
  {
    date: '2025-03-05',
    category: '登壇・セミナー',
    title: '熊本電気工事協同組合の生成AI活用セミナーに講師として登壇しました',
  },
  {
    date: '2024-05-17',
    category: 'メディア掲載',
    outlet: '熊本日日新聞',
    title: '「ChatGPTで業務効率化を 熊本市でプレジ会員向けセミナー」— 熊日プレジデント倶楽部での講演が掲載されました',
    url: 'https://kumanichi.com/articles/1435479',
  },
  {
    date: '2023-12-13',
    category: '登壇・セミナー',
    outlet: 'XOSS POINT.',
    title: '「仕事に活かすChatGPT勉強会」に代表・末松が講師として登壇しました（開催レポート）',
    url: 'https://xosspoint.jp/event-archive/chatgpt_xosspoint231213/',
  },
  {
    date: '2023-07',
    category: 'お知らせ',
    title: 'WizTry株式会社を設立しました',
  },
];

export const YOUTUBE = {
  name: 'KOTARO AI & VIDEO',
  url: 'https://www.youtube.com/@aivideo_biz',
  description:
    '代表・末松が、生成AIの最新動向と実務での使いこなしを動画で発信するYouTubeチャンネル。AI活用のヒントを分かりやすくお届けします。',
};

export const NAV = [
  { href: '/service/', label: 'サービス' },
  { href: '/works/', label: '導入実績' },
  { href: '/about/', label: '会社案内' },
  { href: '/blog/', label: 'ブログ' },
];
