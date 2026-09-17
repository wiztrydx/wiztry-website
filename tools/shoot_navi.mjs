import { chromium } from 'playwright';
const out = process.argv[2];
const jobs = [
  ['ouen-top', 'https://kumamoto-ouen.jp/', 'mobile', 1600],
  ['ouen-ouenwari', 'https://kumamoto-ouen.jp/ouenwari/', 'mobile', 1600],
  ['ouen-yado', 'https://kumamoto-ouen.jp/ouenwari/yado/', 'mobile', 1600],
  ['ouen-wari', 'https://kumamoto-ouen.jp/wari/', 'mobile', 1600],
  ['ouen-map', 'https://kumamoto-ouen.jp/map/', 'mobile', 844],
  ['ouen-top-desktop', 'https://kumamoto-ouen.jp/', 'desktop', 900],
  ['shien-top', 'https://kumamoto-shien.jp/', 'mobile', 1600],
  ['shien-map', 'https://kumamoto-shien.jp/support-map', 'mobile', 844],
];
const browser = await chromium.launch({ channel: 'chrome' });
for (const [name, url, mode, maxH] of jobs) {
  const ctx = await browser.newContext(mode === 'mobile'
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, reducedMotion: 'reduce', locale: 'ja-JP' }
    : { viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1.5, reducedMotion: 'reduce', locale: 'ja-JP' });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    await page.waitForTimeout(2500);
    await page.evaluate(async () => { window.scrollTo(0, document.body.scrollHeight); await new Promise(r => setTimeout(r, 800)); window.scrollTo(0, 0); });
    await page.waitForTimeout(800);
    const h = Math.min(await page.evaluate(() => document.documentElement.scrollHeight), maxH);
    await page.screenshot({ path: `${out}/${name}.png`, clip: { x: 0, y: 0, width: mode === 'mobile' ? 390 : 1280, height: h } });
    console.log('OK', name, h);
  } catch (e) { console.log('FAIL', name, String(e).slice(0, 200)); }
  await ctx.close();
}
await browser.close();
