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

    # ✅ **Unique Chrome Profile for Every Session**
    profile_path = f"/tmp/chrome_profile_{int(time.time())}"
    chrome_options.add_argument(f"--user-data-dir={profile_path}")

    try:
        print("🚀 Launching Chrome for manual login...")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.facebook.com")

        print("⏳ Waiting for manual login (30 sec)...")
        time.sleep(30)  # **Manual login ka wait**

        if "home" in driver.current_url:
            print("✅ Facebook session started successfully!")
            return driver
        else:
            print("❌ Login Failed! Try Again.")
            driver.quit()
            return None
    except Exception as e:
        print(f"⚠️ Error while launching Chrome: {e}")
        return None
