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
    """Check Facebook login using cookies and return session."""
    cookies = load_cookies()
    if not cookies:
        return None

    session = requests.Session()

    # ✅ **Correct Cookies Format**
    for cookie in cookies:
        session.cookies.set(cookie["key"], cookie["value"], domain=cookie["domain"])

    # ✅ **Facebook ko lagna chahiye ki hum real user hai**
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.facebook.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    response = session.get("https://www.facebook.com", headers=headers, allow_redirects=True)

    if "home_icon" in response.text or "profile.php" in response.url:
        print("🎉 Successfully logged in to Facebook!")
        return session
    else:
        print("❌ Login failed! Cookies expire ho sakti hain ya Facebook block kar raha hai.")
        return None

if __name__ == "__main__":
    check_facebook_login()
