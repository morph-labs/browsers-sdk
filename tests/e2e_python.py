import os
import time
from browsers_sdk.client import AuthenticatedClient
from browsers_sdk.api.default import sign_up, create_session, stop_session


def main():
    base_url = os.environ.get("BROWSERS_BASE_URL", "https://browsers.svc.cloud.morph.so")
    token = os.environ.get("MORPH_API_KEY")
    if not token:
        print("MORPH_API_KEY not set; skipping")
        return 0

    client = AuthenticatedClient(base_url=base_url, token=token)

    # Ensure user is enabled
    r = sign_up.sync(client=client)
    print("sign_up:", r)

    sess = create_session.sync(client=client)
    print("session:", sess)

    # Connect via Playwright
    cu = getattr(sess, "connect_url", None) or sess.get("connect_url") if isinstance(sess, dict) else None
    if not cu or "devtools/browser/" not in cu:
        raise SystemExit("Invalid connect_url")

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(cu)
        page = browser.new_page()
        page.goto("https://example.com", timeout=60000)
        print("title:", page.title())
        browser.close()

    stop_session.sync(client=client, id=sess.id if hasattr(sess, "id") else sess["id"])  # type: ignore
    print("stopped:", sess.id if hasattr(sess, "id") else sess["id"])  # type: ignore
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

