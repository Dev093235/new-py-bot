import json
import requests

def load_cookies(file_path="data/cookies.json"):
    """Load cookies from JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)  # Ensure it's a dictionary, not a list!
    except Exception as e:
        print(f"❌ Error: Cookies load nahi ho rahi! ({e})")
        return None

def check_facebook_login():
    """Check Facebook login using cookies and return session."""
    cookies = load_cookies()
    if not cookies or "c_user" not in cookies or "xs" not in cookies:
        print("❌ Error: Cookies.json me c_user ya xs missing hai!")
        return None

    session = requests.Session()
    
    # ✅ **Facebook cookies ko set karo (Safe Method)**
    session.cookies.set("c_user", cookies["c_user"], domain=".facebook.com", path="/")
    session.cookies.set("xs", cookies["xs"], domain=".facebook.com", path="/")

    # ✅ **Facebook ko real user lagna chahiye (Fake Headers)**
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.facebook.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    response = session.get("https://www.facebook.com/", headers=headers, allow_redirects=True)

    if "home_icon" in response.text or "profile.php" in response.url:
        print("🎉 Successfully logged in to Facebook!")
        return session
    else:
        print("❌ Login failed! Cookies expire ho sakti hain ya Facebook block kar raha hai.")
        return None

if __name__ == "__main__":
    check_facebook_login()
