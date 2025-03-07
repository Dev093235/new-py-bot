import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# ✅ **Manual Login Session Handler**
def get_facebook_session():
    """Manually login to Facebook and return session cookies."""
    try:
        # 🔹 **Step 1: Setup Chrome WebDriver**
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Headless mode (background)
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        # 🔹 **Step 2: Open Facebook Login Page**
        print("🌐 Opening Facebook for manual login...")
        driver.get("https://www.facebook.com")
        time.sleep(10)  # Wait for manual login

        # 🔹 **Step 3: Wait Until Logged In**
        while "home.php" not in driver.current_url:
            print("⏳ Waiting for manual login...")
            time.sleep(5)

        print("✅ Facebook login detected! Extracting cookies...")

        # 🔹 **Step 4: Extract Session Cookies**
       
