import bot.fb_login
import bot.auto_reply
import bot.meme_sender
import bot.name_detect
import bot.voice_reply
import time
import requests
import psutil

def check_internet():
    """Check if internet is working"""
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def check_memory_usage():
    """Check if bot is consuming too much memory"""
    memory = psutil.virtual_memory()
    print(f"💾 Memory Usage: {memory.percent}%")
    if memory.percent > 80:  # Agar 80% se zyada memory ho gayi to warning do
        print("⚠️ Warning: High Memory Usage!")

if __name__ == "__main__":
    print("🔥 Mohit Bot Starting...")

    while True:
        try:
            # **Check Internet Connection**
            if not check_internet():
                print("❌ Internet Disconnected! Retrying in 10 seconds...")
                time.sleep(10)
                continue

            # **Facebook Login Check**
            if not bot.fb_login.check_facebook_login():
                print("❌ Login Failed! Cookies Expire Ho Sakti Hain.")
                time.sleep(30)
                continue
            else:
                print("✅ Login Successful!")

            # **Bot Loop**
            while True:
                try:
                    messages = [("Hello bot!", "Rahul"), ("Kya haal hai?", "Pooja")]

                    bot.auto_reply.check_messages(messages)
                    bot.meme_sender.send_meme()
                    bot.name_detect.detect_name()
                    bot.voice_reply.voice_response()

                    check_memory_usage()  # **Memory Check**
                    time.sleep(5)

                except Exception as e:
                    print(f"⚠️ Error in Bot Loop: {e}")
                    time.sleep(5)  # Error ke baad retry karo

        except Exception as e:
            print(f"⚠️ Fatal Error: {e}")
            time.sleep(10)  # Fatal error ke baad 10 sec me restart karo
