import json
import requests

def load_cookies(file_path="data/cookies.json"):
    """Load cookies from JSON file in correct format."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            cookies = json.load(f)

        # Check if necessary cookies exist
        if "c_user" not in cookies or "xs" not in cookies:
            raise Exception("❌ Invalid cookies format! Make sure `c_user` and `xs` are present.")

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

    # ✅ Set cookies correctly
    session.cookies.set("c_user", cookies["c_user"], domain=".facebook.com")
    session.cookies.set("xs", cookies["xs"], domain=".facebook.com")

    # ✅ Set headers to mimic real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.facebook.com/",
    }

    response = session.get("https://www.facebook.com", headers=headers, allow_redirects=True)

    if "home_icon" in response.text or "profile.php" in response.url:
        print("🎉 Successfully logged in to Facebook!")
        return session
    else:
        print("❌ Login failed! Cookies expire ho sakti hain ya format galat hai.")
        return None

if __name__ == "__main__":
    check_facebook_login()
