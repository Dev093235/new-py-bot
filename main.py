import bot.fb_login
import bot.auto_reply
import bot.meme_sender
import bot.name_detect
import bot.voice_reply
import time

if __name__ == "__main__":
    print("🔥 Mohit Bot Starting...")

    # Facebook login check
    if not bot.fb_login.check_facebook_login():
        print("❌ Login failed! Cookies expire ho sakti hain.")
    else:
        print("✅ Login successful!")

    while True:
        try:
            # Example messages list (isey tum actual inbox se fetch kar sakte ho)
            messages = [("Hello bot!", "Rahul"), ("Kya haal hai?", "Pooja")]

            # Bot functions ko run karo
            bot.auto_reply.check_messages(messages)
            bot.meme_sender.send_meme()
            bot.name_detect.detect_name()
            bot.voice_reply.voice_response()

            time.sleep(5)  # 5 sec delay to avoid spam

        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(5)  # Error ke baad bhi bot loop me rahe
