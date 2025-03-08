from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def get_facebook_session():
    """Firefox ke saath Facebook Manual Login Enable Karega"""
    options = Options()
    options.binary_location = "/usr/bin/firefox"  # Ensure karo yeh correct ho
    options.add_argument("--headless")  # GUI nahi chahiye to enable karo
    options.add_argument("--disable-gpu")

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.facebook.com")

    print("⏳ Waiting for manual login (40 sec)...")
    time.sleep(40)  # **Tumhe manually login karna hoga**

    if "home" in driver.current_url:
        print("✅ Facebook session started successfully!")
        return driver
    else:
        print("❌ Login Failed! Try Again.")
        driver.quit()
        return None
