import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 🔑 Facebook Credentials (Yeh GitHub Secrets ya `.env` file me store karo)
EMAIL = "your_email_here"
PASSWORD = "your_password_here"

def login_facebook():
    """Email aur Password se Facebook Login"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 🖥 Background Mode (Optional)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ✅ Chrome Driver Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.facebook.com")

    # 🟢 Email Input
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(EMAIL)

    # 🔵 Password Input
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)  # ⏳ Wait for Login

    # ✅ **Login Success Check**
    if "home_icon" in driver.page_source or "profile.php" in driver.current_url:
        print("🎉 Successfully Logged into Facebook!")

        # ✅ **Cookies Save Karo**
        cookies = driver.get_cookies()
        with open("data/cookies.json", "w") as file:
            json.dump(cookies, file)

        print("✅ Cookies Saved Successfully!")
        driver.quit()
        return True
    else:
        print("❌ Login Failed! Invalid Credentials or Security Check Required.")
        driver.quit()
        return False

# 🏁 **Run Login**
if __name__ == "__main__":
    login_facebook()
