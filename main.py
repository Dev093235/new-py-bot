import bot.fb_login
import bot.auto_reply
import bot.meme_sender
import bot.name_detect
import bot.voice_reply
import time

if __name__ == "__main__":
    print("🔥 Mohit Bot Starting...")

    # Facebook login check
    try:
        if not bot.fb_login.check_facebook_login():
            print("❌ Login failed! Cookies expire ho sakti hain.")
            exit()  # Agar login fail ho jaye to bot exit kar de
        else:
            print("✅ Login successful!")
    except AttributeError:
        print("⚠️ Error: 'check_facebook_login()' function missing in fb_login.py!")
        exit()

    while True:
        try:
            # Inbox se messages fetch karo (Isko tum apni API ya web scraper se connect kar sakte ho)
            messages = [
                ("Hello bot!", "Rahul"),
                ("Kya haal hai?", "Pooja")
            ]

            # Check karo ki `auto_reply` module me `check_messages()` function hai ya nahi
            if hasattr(bot.auto_reply, 'check_messages'):
                bot.auto_reply.check_messages(messages)
            else:
                print("⚠️ Error: 'check_messages()' function missing in auto_reply.py!")

            # Baaki bot features ko execute karo
            bot.meme_sender.send_meme()
            bot.name_detect.detect_name()
            bot.voice_reply.voice_response()

            time.sleep(5)  # 5 sec delay to avoid spam

        except Exception as e:
            print(f"⚠️ Unexpected Error: {e}")
            time.sleep(5)  # Error ke baad bhi bot loop me chalta rahe
