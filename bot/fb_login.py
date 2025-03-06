import json
import requests

def load_cookies(file_path="data/cookies.json"):
    """Load cookies from JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            cookies = json.load(f)
        return cookies
    except Exception as e:
        print(f"❌ Error: Cookies load nahi ho rahi! ({e})")
        return None

def check_facebook_login():
    """Check if Facebook login is successful using cookies."""
    cookies = load_cookies()
    if not cookies:
        return False
    
    session = requests.Session()
    session.cookies.update(cookies)

    response = session.get("https://www.facebook.com", allow_redirects=True)

    if "home_icon" in response.text or "profile.php" in response.url:
        print("🎉 Successfully logged in to Facebook!")
        return True
    else:
        print("❌ Login failed! Cookies expire ho sakti hain.")
        return False

if __name__ == "__main__":
    check_facebook_login()
