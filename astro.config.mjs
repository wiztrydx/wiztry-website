import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://wiztrydx.com',
  integrations: [sitemap()],
  build: {
    inlineStylesheets: 'auto',
  },
});
