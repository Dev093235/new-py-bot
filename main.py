import bot.fb_login
import bot.auto_reply
import bot.meme_sender
import bot.name_detect
import bot.voice_reply
import time

if __name__ == "__main__":
    print("🔥 Mohit Bot Starting...")
    bot.fb_login.login()
    
    while True:
        bot.auto_reply.check_messages()
        bot.meme_sender.send_meme()
        bot.name_detect.detect_name()
        bot.voice_reply.voice_response()
        time.sleep(5)  # 5 sec delay to avoid spam
