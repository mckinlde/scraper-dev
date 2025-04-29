# scraper/hello_world.py

from scraper.headless_browser import get_driver as get_headless_driver
from scraper.browser import get_driver as get_windowed_driver

def test_driver(driver_func, description):
    driver = driver_func()
    driver.get("https://example.com")
    title = driver.title
    driver.quit()
    assert "Example Domain" in title, f"{description} failed: Unexpected title '{title}'"
    print(f"{description}: PASS")

def main():
    test_driver(get_headless_driver, "Headless Chrome")
    test_driver(get_windowed_driver, "Windowed Chrome")

if __name__ == "__main__":
    main()
