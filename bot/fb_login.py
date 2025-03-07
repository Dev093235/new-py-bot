import time
import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_facebook_session():
    """Open Chrome and wait for manual Facebook login."""
    options = Options()
    
    # ✅ **Fix: Unique User Data Directory**
    user_data_dir = f"/tmp/chrome_user_data_{random.randint(1000, 9999)}"
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # ✅ **Prevent Bot Detection**
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")

    # ✅ **Run Headed Mode for Manual Login**
    options.add_experimental_option("detach", True)

    # ✅ **Initialize Chrome Driver**
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.facebook.com")

    print("⏳ Waiting for manual login...")
    input("✔️ Press Enter after logging in to continue...")  

    print("✅ Login detected! Continuing bot execution...")
    return driver

if __name__ == "__main__":
    session = get_facebook_session()
