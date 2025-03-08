from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def get_facebook_session():
    """Manual Facebook login ke liye Chrome launch karega."""

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")

    # ✅ **Headless Mode HATAO**
    # chrome_options.add_argument("--headless=new")  # ❌ Isko hata do!

    # ✅ **Use Existing Chrome Profile**
    profile_path = os.path.expanduser("~/.config/google-chrome/Default")
    chrome_options.add_argument(f"--user-data-dir={profile_path}")

    try:
        print("🚀 Launching Chrome for manual login...")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.facebook.com")

        print("⏳ Checking if already logged in...")
        time.sleep(10)  # Wait for the page to load

        if "home" in driver.current_url:
            print("✅ Facebook session detected! Bot is ready.")
            return driver
        else:
            print("❌ Login Failed! Please manually log in and try again.")
            driver.quit()
            return None
    except Exception as e:
        print(f"⚠️ Error while launching Chrome: {e}")
        return None
