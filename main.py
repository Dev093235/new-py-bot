from bot.fb_login import get_facebook_session
import time

print("🔥 Mohit Bot Starting...")
session = get_facebook_session()

if not session:
    print("❌ Exiting... Login Failed.")
else:
    print("✅ Successfully Logged in!")
