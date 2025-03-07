from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def get_facebook_session():
    """Start Chrome with a unique user data directory to prevent session conflicts."""
    chrome_options = Options()
    
    # ✅ Important: Unique user-data-dir use karein
    chrome_options.add_argument("--user-data-dir=/tmp/chrome_user_data")  
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # ✅ Chrome Driver Initialize
    service = Service("/usr/bin/chromedriver")  # ✅ ChromeDriver ka path ensure karein
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # ✅ Open Facebook Login Page
    driver.get("https://www.facebook.com")
    
    print("⏳ Waiting for manual login...")
    time.sleep(30)  # 30 seconds rukne do taaki aap manually login kar sakein

    print("✅ Facebook session started!")
    return driver

if __name__ == "__main__":
    get_facebook_session()
