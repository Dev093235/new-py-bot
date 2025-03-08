from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
import shutil

def get_facebook_session():
    """Start Chrome with a unique user data directory to prevent session conflicts."""
    chrome_options = Options()

    # 🔄 **Temporary Folder for Chrome Profile** (Automatically Clears Old Data)
    temp_dir = "/tmp/chrome_fb_session"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)  # ✅ Purane session data ko delete karo

    chrome_options.add_argument(f"--user-data-dir={temp_dir}")  
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # ✅ **Chrome Driver Initialize**
    service = Service("/usr/bin/chromedriver")  
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # ✅ **Open Facebook Login Page**
    driver.get("https://www.facebook.com")
    
    print("⏳ Waiting for manual login (30s)...")
    time.sleep(30)  # ⏳ **Manually login karne ka time**

    print("✅ Facebook session started!")
    return driver

if __name__ == "__main__":
    get_facebook_session()
