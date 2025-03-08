from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def manual_facebook_login():
    """Firefox browser launch karega aur aap manually login kar sakte hain"""
    options = Options()
    options.headless = False  # Headless mode OFF karein taki browser dikh sake

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.facebook.com")

    print("⏳ Please manually login to Facebook... (Waiting for 60 seconds)")
    time.sleep(60)  # Aapko 60 seconds milenge login karne ke liye

    if "home" in driver.current_url:
        print("✅ Facebook login successful!")
        return driver
    else:
        print("❌ Login failed! Please try again.")
        driver.quit()
        return None

if __name__ == "__main__":
    print("🔥 Starting Bot...")
    session = manual_facebook_login()
    if session:
        print("🚀 Bot Started Successfully!")
    else:
        print("❌ Bot Failed to Start.")
