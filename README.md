# Browsers SDK

SDKs for the Morph Browsers service generated from OpenAPI via Fern.

## Install (Python)

Use directly from Git for now (until published):

```
uv add "browsers-sdk @ git+https://github.com/morph-labs/browsers-sdk.git@main#subdirectory=sdks/python"
```

## Generate SDKs

```
BASE_URL ?= https://browsers.svc.cloud.morph.so
make generate-python-sdk
```

This will fetch the OpenAPI from the running service and generate clients into `sdks/python` and `sdks/typescript` (configurable in `fern/generators.yml`).

## Example (Python + Playwright)

```python
import os
from browsers_sdk import BrowsersApi  # generated package name may vary
from playwright.sync_api import sync_playwright

api = BrowsersApi(base_url=os.environ.get("MORPH_BROWSERS_BASE_URL", "https://browsers.svc.cloud.morph.so"), token=os.environ["MORPH_API_KEY"])  # bearer auth
sess = api.create_session(name="demo")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(sess.connect_url)
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()

api.stop_session(sess.id)
```

## Example (TypeScript + Playwright)

```ts
import { chromium } from 'playwright';
import { BrowsersApi } from './sdks/typescript';

const api = new BrowsersApi({ baseUrl: process.env.BROWSERS_BASE_URL!, token: process.env.MORPH_API_KEY! });
const sess = await api.createSession({ name: 'demo' });

const browser = await chromium.connectOverCDP(sess.connectUrl);
const page = await browser.newPage();
await page.goto('https://example.com');
console.log(await page.title());
await browser.close();

await api.stopSession(sess.id);
```

## CI + Publish

- SDKs are auto-regenerated on changes to `fern/**` via `.github/workflows/generate.yml`.
- Publishing is triggered on GitHub releases:
  - PyPI: `.github/workflows/publish-python.yml` expects `PYPI_API_TOKEN` in repo secrets.
  - npm: `.github/workflows/publish-npm.yml` expects `NPM_TOKEN` in repo secrets.
