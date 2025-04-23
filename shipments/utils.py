from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json
import logging

def fetch_shipments_with_js():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            try:
                page.goto("https://censibal.github.io/txr-technical-hiring/", timeout=60000)
                page.wait_for_selector("#json", timeout=10000)
                json_text = page.locator("#json").inner_text()
                data = json.loads(json_text)
                return data.get("shipments", [])
            except PlaywrightTimeoutError:
                logging.error("Timeout while loading the page or waiting for selector.")
            except json.JSONDecodeError as e:
                logging.error(f"Error decoding JSON: {e}")
            except Exception as e:
                logging.error(f"Unexpected error while fetching data: {e}")
            finally:
                browser.close()
    except Exception as e:
        logging.error(f"Failed to initialize Playwright: {e}")
    
    return []  # Return an empty list on failure
