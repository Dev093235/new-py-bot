import json
import requests

# ✅ Facebook Login Credentials
FB_EMAIL = "royvashu752@gmail.com"  # 🔄 Apna email daalo
FB_PASSWORD = "mohit1234"  # 🔄 Apna password daalo

def login_with_email_password(email, password):
    """Facebook Login using Email & Password (Safe Method)"""
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    login_url = "https://www.facebook.com/login.php"
    data = {
        "email": email,
        "pass": password
    }

    response = session.post(login_url, data=data, headers=headers)

    # ✅ Check Login Success
    if "home_icon" in response.text or "profile.php" in response.url:
        print("🎉 Successfully logged in to Facebook!")
        return session
    else:
        print("❌ Login failed! Check Email/Password or CAPTCHA Verification.")
        return None

if __name__ == "__main__":
    session = login_with_email_password(FB_EMAIL, FB_PASSWORD)
    if session:
        print("✅ Session Ready! Now you can automate tasks.")
