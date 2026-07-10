import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://wiztrydx.com',
  // リンクを画面に入った時点で先読み → ページ遷移が体感ゼロ秒になる
  prefetch: { prefetchAll: true, defaultStrategy: 'viewport' },
  integrations: [
    sitemap({
      // noindexページはサイトマップからも除外する
      filter: (page) => !page.includes('/contact/thanks/'),
    }),
  ],
  build: {
    inlineStylesheets: 'auto',
  },
});
