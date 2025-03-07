import time
import requests
import sys

try:
    import psutil
except ImportError:
    print("⚠️ 'psutil' module missing! Installing now...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil

from bot.fb_login import get_facebook_session
import bot.auto_reply
import bot.meme_sender
import bot.name_detect
import bot.voice_reply

def check_internet():
    """Check if internet is working."""
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def check_memory_usage():
    """Check if bot is consuming too much memory."""
    memory = psutil.virtual_memory()
    print(f"💾 Memory Usage: {memory.percent}%")
    if memory.percent > 80:
        print("⚠️ Warning: High Memory Usage!")

if __name__ == "__main__":
    print("🔥 Mohit Bot Starting...")

    start_time = time.time()
    timeout = 300  # 5 minutes timeout

    while True:
        try:
            if time.time() - start_time > timeout:
                print("⏳ Timeout Reached! Exiting...")
                break

            if not check_internet():
                print("❌ Internet Disconnected! Retrying in 10 seconds...")
                time.sleep(10)
                continue

            session = get_facebook_session()  # ✅ Manually Login to Facebook
            if not session:
                print("❌ Login Failed! Try Again.")
                time.sleep(30)
                continue
            else:
                print("✅ Login Successful!")

            while True:
                try:
                    messages = [("Hello bot!", "Rahul"), ("Kya haal hai?", "Pooja")]

                    bot.auto_reply.check_messages(session, messages)  # ✅ Pass session
                    bot.meme_sender.send_meme(session)  # ✅ Pass session
                    bot.name_detect.detect_name()
                    bot.voice_reply.voice_response()

                    check_memory_usage()
                    time.sleep(5)

                    if time.time() - start_time > timeout:
                        print("⏳ Timeout Reached! Exiting Inner Loop...")
                        break

                except Exception as e:
                    print(f"⚠️ Error in Bot Loop: {e}")
                    time.sleep(5)

        except Exception as e:
            print(f"⚠️ Fatal Error: {e}")
            time.sleep(10)
