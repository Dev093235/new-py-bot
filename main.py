import json
import requests

def load_cookies(file_path="data/cookies.json"):
    """Load cookies from JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            cookies = json.load(f)
        if not cookies:
            raise Exception("Cookies file empty! Please add valid Facebook cookies.")
        return cookies
    except Exception as e:
        print(f"❌ Error: Cookies load nahi ho rahi! ({e})")
        return None

def check_facebook_login():
    """Check Facebook login using cookies."""
    cookies = load_cookies()
    if not cookies:
        return False

    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie["key"], cookie["value"], domain=cookie["domain"])

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    response = session.get("https://www.facebook.com", headers=headers, allow_redirects=True)

    if "home_icon" in response.text or "profile.php" in response.url:
        print("🎉 Successfully logged in to Facebook!")
        return session
    else:
        print("❌ Login failed! Cookies expire ho sakti hain.")
        return None

if __name__ == "__main__":
    check_facebook_login()
