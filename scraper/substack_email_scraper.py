import re
import time
import traceback
from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraper.headless_browser import get_driver  # Your existing module

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
KEYWORDS = ["about", "contact", "press", "team"]

def extract_newsletter_links(driver):
    print("🔎 Visiting leaderboard...")
    driver.get("https://substack.com/leaderboard/us-politics/paid")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href^='/@']"))
        )
        links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/@']")
        urls = ["https://substack.com" + a.get_attribute("href") for a in links]
        print(f"✅ Found {len(urls)} newsletter links")
        return list(set(urls))  # de-duplicate
    except Exception:
        print("❌ Could not load leaderboard entries")
        traceback.print_exc()
        return []

def extract_emails_from_page(driver, url):
    try:
        print(f"🌐 Visiting {url}")
        driver.get(url)
        time.sleep(2)
        body = driver.find_element(By.TAG_NAME, "body")
        emails = EMAIL_REGEX.findall(body.text)
        print(f"📧 Found {len(emails)} emails on {url}")
        return emails
    except Exception:
        print(f"❌ Error extracting from {url}")
        traceback.print_exc()
        return []

def find_contact_pages(driver, base_url):
    try:
        print(f"🔗 Finding contact/about links on {base_url}")
        links = driver.find_elements(By.TAG_NAME, "a")
        contact_urls = []
        for link in links:
            href = link.get_attribute("href")
            if not href:
                continue
            text = link.text.lower()
            if any(k in text or k in href.lower() for k in KEYWORDS):
                contact_urls.append(urljoin(base_url, href))
        unique_links = list(set(contact_urls))
        print(f"🔍 Found {len(unique_links)} contact-like pages")
        return unique_links
    except Exception:
        print(f"⚠️ Failed to extract contact links from {base_url}")
        traceback.print_exc()
        return []

def guess_email_from_substack_url(url):
    match = re.search(r"substack\.com/@([a-zA-Z0-9_.+-]+)", url)
    if match:
        return f"{match.group(1)}@substack.com"
    return None

def main():
    driver = get_driver()
    try:
        newsletter_links = extract_newsletter_links(driver)
        all_results = {}

        for link in newsletter_links:
            print(f"\n==============================\n🔎 Processing: {link}")
            found_emails = set()

            # Step 1: Check main page
            found_emails.update(extract_emails_from_page(driver, link))

            # Step 2: Check about/contact pages
            contact_pages = find_contact_pages(driver, link)
            for page in contact_pages:
                found_emails.update(extract_emails_from_page(driver, page))

            # Step 3: Fallback to inferred email
            if not found_emails:
                fallback = guess_email_from_substack_url(link)
                if fallback:
                    print(f"📨 Using fallback email: {fallback}")
                    found_emails.add(fallback)

            if found_emails:
                all_results[link] = list(found_emails)
                print(f"✅ ✅ ✅ Emails for {link}:\n{list(found_emails)}")
            else:
                print(f"🚫 No emails found for {link}")

    finally:
        print("\n📴 Quitting browser...")
        driver.quit()

if __name__ == "__main__":
    main()
