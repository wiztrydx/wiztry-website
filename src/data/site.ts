// サイト全体で使う共通データ。数字・社名を更新するときはこのファイルだけ直す。

export const SITE = {
  name: 'WizTry株式会社',
  nameEn: 'WizTry Inc.',
  domain: 'https://wiztrydx.com',
  email: 'info@wiztrydx.com',
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
  { slug: 'kumanichi', name: '株式会社熊本日日新聞社', shape: 'wide' },
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
  { slug: 'aoyagi', name: '有限会社青柳', shape: 'square' },
  { slug: 'carepark', name: '株式会社ケアパーク', shape: 'wide' },
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

export const MEDIA = [
  {
    title: '「挫折を原点に、挑戦し続けてきた先に見えた景色とは」代表・末松のインタビュー',
    outlet: 'Muse',
    url: 'https://www.my-muse.jp/people/kotaro_suematsu/',
  },
  {
    title: 'ChatGPTで業務効率化を 熊本市でプレジ会員向けセミナー',
    outlet: '熊本日日新聞',
    url: 'https://kumanichi.com/articles/1435479',
  },
  {
    title: '【実演あり】仕事に活かすChatGPT勉強会 開催レポート',
    outlet: 'XOSS POINT.',
    url: 'https://xosspoint.jp/event-archive/chatgpt_xosspoint231213/',
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
