from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def login_facebook(email, password):
    """Manually login to Facebook and let bot continue."""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-data-dir=/tmp/chrome_profile")  # ✅ Unique path

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.facebook.com")
    time.sleep(10)  # 10 seconds wait for manual login

    input("🔵 Press Enter after completing the login manually...")

    print("✅ Login Successful! Bot is now running.")
    return driver

if __name__ == "__main__":
    EMAIL = "your-email@example.com"
    PASSWORD = "your-password"
    driver = login_facebook(EMAIL, PASSWORD)
