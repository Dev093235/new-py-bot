from bot.fb_login import check_facebook_login
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
    if memory.percent > 80:
        print("⚠️ Warning: High Memory Usage!")

if __name__ == "__main__":
    print("🔥 Mohit Bot Starting...")

    start_time = time.time()  
    timeout = 300  # 5 minutes timeout

    # **Check Internet Connection**
    if not check_internet():
        print("❌ Internet Disconnected! Exiting...")
        exit(1)

    # **Facebook Login Check**
    session = check_facebook_login()  
    if not session:
        print("❌ Login Failed! Cookies might be expired.")
        exit(1)

    print("✅ Login Successful!")

    # **Bot Loop**
    while True:
        try:
            # **Fetch New Messages**
            messages = bot.auto_reply.check_messages(session)
            for msg in messages:
                try:
                    if isinstance(msg, tuple) and len(msg) == 2:
                        user_id, message_text = msg
                        print(f"📩 Message from {user_id}: {message_text}")

                        # **Bot Replies**
                        bot.auto_reply.send_reply(session, user_id, message_text)
                        bot.meme_sender.send_meme(session, user_id)
                        bot.name_detect.detect_name(session, user_id, message_text)
                        bot.voice_reply.voice_response(session, user_id, message_text)

                        check_memory_usage()
                        time.sleep(3)  # Delay between responses
                    else:
                        print(f"⚠️ Unexpected message format: {msg}")
                except Exception as e:
                    print(f"⚠️ Error handling message: {e}")

            # **Timeout Check**
            if time.time() - start_time > timeout:
                print("⏳ Timeout Reached! Exiting...")
                break

            time.sleep(5)  # **Main loop delay**

        except Exception as e:
            print(f"⚠️ Fatal Error: {e}")
            time.sleep(10)  # **Retry after 10 seconds**
