import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_facebook_session():
    """Manually login detect karne ka function"""
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=/tmp/chrome_data")  # Use existing session
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.facebook.com")
    
    for _ in range(30):  # 30 baar check karega (30 sec tak)
        time.sleep(1)
        if "home_icon" in driver.page_source:
            print("✅ Login successful! Closing browser...")
            cookies = driver.get_cookies()
            driver.quit()
            return cookies  # Cookies return karega
        else:
            print("⏳ Waiting for manual login...")

    print("❌ Manual login failed! Exiting...")
    driver.quit()
    return None
