import json
import bot.fb_login
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

def check_facebook_login():
    """Cookies se login check karo, agar fail ho to email/password se login karo"""
    try:
        with open("data/cookies.json", "r") as file:
            cookies = json.load(file)

        if not cookies:
            raise Exception("Cookies file empty
