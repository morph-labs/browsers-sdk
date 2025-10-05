// ESM test using the generated TypeScript SDK and Playwright
import { chromium } from 'playwright';
import { OpenAPI } from '../sdks/typescript/core/OpenAPI.js';
import { AxiosHttpRequest } from '../sdks/typescript/core/AxiosHttpRequest.js';
import { DefaultService } from '../sdks/typescript/services/DefaultService.js';

const BASE = process.env.BROWSERS_BASE_URL || 'https://browsers.svc.cloud.morph.so';
const TOKEN = process.env.MORPH_API_KEY;
if (!TOKEN) {
  console.log('MORPH_API_KEY not set; skipping');
  process.exit(0);
}

OpenAPI.BASE = BASE;
OpenAPI.TOKEN = TOKEN;

const svc = new DefaultService(new AxiosHttpRequest(OpenAPI));

// Enable user (idempotent)
await svc.signUp();

// Create session
const sess = await svc.createSession();
if (!sess.connect_url || !sess.connect_url.includes('devtools/browser/')) {
  throw new Error('Invalid connect_url');
}

const browser = await chromium.connectOverCDP(sess.connect_url);
const page = await browser.newPage();
await page.goto('https://example.com', { timeout: 60000 });
console.log('title:', await page.title());
await browser.close();

await svc.stopSession(sess.id);
console.log('stopped:', sess.id);

