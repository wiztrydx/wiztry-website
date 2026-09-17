// ローカル開発サーバーのページをフルページ撮影してタイル分割する（表示検証用）
import { chromium } from 'playwright';
import fs from 'node:fs';
const out = process.argv[2];
const base = 'http://localhost:4321';
const paths = process.argv.slice(3);
const browser = await chromium.launch({ channel: 'chrome' });
for (const mode of ['desktop', 'mobile']) {
  const ctx = await browser.newContext(mode === 'mobile'
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true, reducedMotion: 'reduce', locale: 'ja-JP' }
    : { viewport: { width: 1366, height: 900 }, deviceScaleFactor: 1, reducedMotion: 'reduce', locale: 'ja-JP' });
  for (const p of paths) {
    const page = await ctx.newPage();
    try {
      await page.goto(base + p, { waitUntil: 'networkidle', timeout: 60000 });
      await page.waitForTimeout(1200);
      // 出現アニメを全部済ませる
      await page.evaluate(async () => {
        document.querySelectorAll('.reveal').forEach((el) => el.classList.add('is-in'));
        const h = document.body.scrollHeight;
        for (let y = 0; y < h; y += 600) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60)); }
        window.scrollTo(0, 0);
      });
      await page.waitForTimeout(800);
      const name = (p.replace(/\//g, '_').replace(/^_|_$/g, '') || 'home') + '-' + mode;
      await page.screenshot({ path: `${out}/${name}.png`, fullPage: true });
      const imgs = await page.evaluate(() => [...document.images].filter((i) => i.complete && i.naturalWidth === 0).map((i) => i.getAttribute('src')));
      console.log('OK', name, imgs.length ? 'BROKEN:' + imgs.join(',') : '');
    } catch (e) { console.log('FAIL', p, mode, String(e).slice(0, 160)); }
    await page.close();
  }
  await ctx.close();
}
await browser.close();
