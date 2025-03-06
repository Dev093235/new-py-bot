import browser_cookie3
import json

def export_cookies():
    """Chrome se Facebook cookies export karne ka function"""
    cookies = browser_cookie3.chrome(domain_name="facebook.com")
    cookie_list = []

    for cookie in cookies:
        cookie_list.append({
            "key": cookie.name,
            "value": cookie.value,
            "domain": cookie.domain,
            "path": cookie.path,
            "hostOnly": cookie.secure
        })

    # ✅ Cookies ko save karna
    with open("data/cookies.json", "w", encoding="utf-8") as f:
        json.dump(cookie_list, f, indent=4)

    print("✅ Chrome Cookies Successfully Exported! Use `cookies.json` in your bot.")

# Run the export function
if __name__ == "__main__":
    export_cookies()
