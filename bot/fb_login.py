from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def get_facebook_session():
    """Manually Facebook login karne ke liye Chrome open karega."""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")  # Allow debugging
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-gpu")

    # 🛠 **Fix for 'user-data-dir' error**
    chrome_options.add_argument("--user-data-dir=/tmp/chrome_profile")  # Unique profile
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.facebook.com")

    print("⏳ Waiting for manual login...")
    time.sleep(30)  # **Wait for manual login**
    
    if "home" in driver.current_url:
        print("✅ Facebook session started!")
        return driver
    else:
        print("❌ Login Failed! Please try again.")
        driver.quit()
        return None
