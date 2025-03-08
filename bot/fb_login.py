from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import shutil

def get_facebook_session():
    """Manual Facebook login ke liye Chrome launch karega."""

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")

    # ✅ **Fix: Unique Chrome Profile Path & Cleanup Old Sessions**
    profile_path = "/tmp/chrome_profile"
    if os.path.exists(profile_path):
        shutil.rmtree(profile_path)  # ❌ Purani session files hata do
    chrome_options.add_argument(f"--user-data-dir={profile_path}")

    try:
        print("🚀 Launching Chrome for manual login...")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.facebook.com")

        print("⏳ Waiting for manual login (40 sec)...")
        time.sleep(40)  # **Manual login ka wait**

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
