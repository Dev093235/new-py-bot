from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle
import time

def manual_facebook_login():
    """Manually login to Facebook in Chrome, and save session."""
    
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)
    driver.get("https://www.facebook.com/")

    print("🔵 Please manually login to Facebook.")
    input("✅ Press Enter after logging in...")

    # Save session cookies
    pickle.dump(driver.get_cookies(), open("data/session.pkl", "wb"))
    print("✅ Session saved successfully!")

    driver.quit()


def load_facebook_session():
    """Load saved Facebook session and continue bot operations."""
    
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)
    driver.get("https://www.facebook.com/")

    # Load saved session
    cookies = pickle.load(open("data/session.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()
    print("✅ Bot is now logged in and ready!")

    return driver


if __name__ == "__main__":
    choice = input("🔹 Type 'login' for manual login OR 'start' to load session: ").strip().lower()
    
    if choice == "login":
        manual_facebook_login()
    elif choice == "start":
        driver = load_facebook_session()
        time.sleep(10)  # Keep session open
        driver.quit()
    else:
        print("❌ Invalid input! Please type 'login' or 'start'.")
