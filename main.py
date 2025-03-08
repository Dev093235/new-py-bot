from bot.fb_login import get_facebook_session
import time

print("🔥 Mohit Bot Starting...")

session = get_facebook_session()
if not session:
    print("❌ Exiting... Login Failed.")
    exit(1)  # 🛑 **Process exit karne ke liye**
else:
    print("✅ Bot is now active!")
    while True:
        print("💬 Bot running... Checking messages!")
        time.sleep(10)  # **10 sec delay to avoid spam**
