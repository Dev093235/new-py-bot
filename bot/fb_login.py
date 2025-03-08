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

    # 🛠 **Fix for 'user-data-dir' error**
    profile_path = f"/tmp/chrome_profile_{int(time.time())}"  # Unique profile path
    chrome_options.add_argument(f"--user-data-dir={profile_path}")

    # ✅ **Use Headless Mode**
    chrome_options.add_argument("--headless=new")  # **Headless mode for GitHub Actions**

    try:
        print("🚀 Launching Chrome for manual login...")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.facebook.com")

        print("⏳ Waiting for manual login (40 sec)...")
        time.sleep(40)  # **Login karne ka time diya**

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
