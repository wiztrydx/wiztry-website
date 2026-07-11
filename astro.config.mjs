import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// 旧Studioサイト時代のURL → 新サイトの対応ページへ転送
// （静的ホスティングのためmeta refresh方式。Googleはこれをリダイレクトとして扱う）
const LEGACY_REDIRECTS = {
  '/service/business-development': '/service/',
  '/service/digital-markting': '/service/',
  '/service/consulting': '/service/',
  '/case': '/works/',
  '/privacy-policy': '/privacy/',
};

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
    }),
  ],
  build: {
    inlineStylesheets: 'auto',
  },
});
