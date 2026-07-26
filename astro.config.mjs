import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { execFileSync } from 'node:child_process';

// 旧Studioサイト時代のURL → 新サイトの対応ページへ転送
// （静的ホスティングのためmeta refresh方式。Googleはこれをリダイレクトとして扱う）
const LEGACY_REDIRECTS = {
  '/service/business-development': '/service/',
  '/service/digital-markting': '/service/',
  '/service/consulting': '/service/',
  '/case': '/works/',
  '/privacy-policy': '/privacy/',
};

// URLごとの実際の更新日時をGit履歴から取得する。
// ビルド日時を使うと、内容が変わっていないページまで毎回更新扱いになるため使わない。
function getSitemapSourcePaths(pageUrl) {
  const pathname = new URL(pageUrl).pathname;

  if (pathname === '/') return ['src/pages/index.astro'];

  if (pathname === '/blog/') {
    // 記事の追加・更新で一覧ページも変わる。
    return ['src/pages/blog/index.astro', 'src/content/blog'];
  }

  const blogMatch = pathname.match(/^\/blog\/([^/]+)\/$/);
  if (blogMatch) {
    // 記事本文と共通記事テンプレートの新しい方を採用する。
    return [`src/content/blog/${blogMatch[1]}.md`, 'src/pages/blog/[...slug].astro'];
  }

  return [`src/pages${pathname}index.astro`];
}

function getGitLastModified(pageUrl) {
  const timestamp = execFileSync(
    'git',
    ['log', '-1', '--format=%cI', '--', ...getSitemapSourcePaths(pageUrl)],
    { encoding: 'utf8' },
  ).trim();

  return timestamp || undefined;
}

export default defineConfig({
  site: 'https://wiztrydx.com',
  redirects: LEGACY_REDIRECTS,
  // リンクを画面に入った時点で先読み → ページ遷移が体感ゼロ秒になる
  prefetch: { prefetchAll: true, defaultStrategy: 'viewport' },
  integrations: [
    sitemap({
      // noindexページ・リダイレクト用スタブはサイトマップから除外する
      filter: (page) =>
        !page.includes('/contact/thanks/') &&
        !Object.keys(LEGACY_REDIRECTS).some((p) => new URL(page).pathname.replace(/\/$/, '') === p),
      serialize: (item) => ({
        ...item,
        lastmod: getGitLastModified(item.url),
      }),
    }),
  ],
  build: {
    inlineStylesheets: 'auto',
  },
});
