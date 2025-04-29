# scraper/hello_world.py

from scraper.browser import get_driver

def main():
    driver = get_driver()
    driver.get("https://example.com")
    print(driver.title)
    driver.quit()

if __name__ == "__main__":
    main()
