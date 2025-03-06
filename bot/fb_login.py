import requests

# Facebook Login Credentials
FB_EMAIL = "royvashu752@gmail.com"
FB_PASSWORD = "mohit1234"

def login_with_password():
    """Facebook login using email & password"""
    session = requests.Session()

    login_url = "https://www.facebook.com/login.php"
    payload = {
        "email": FB_EMAIL,
        "pass": FB_PASSWORD
    }

    response = session.post(login_url, data=payload)

    if "c_user" in session.cookies.get_dict():
        print("🎉 Successfully Logged in to Facebook!")
        return session
    else:
        print("❌ Login Failed! Check email/password.")
        return None

if __name__ == "__main__":
    login_with_password()
