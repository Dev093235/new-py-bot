Agar aap Kiwi Browser se GitHub Actions ko manually control karna chahte hain aur Facebook me manual login bhi karna chahte hain, to aapko GitHub Actions ka YAML file aise setup karna hoga ki:

1. Kiwi Browser me GitHub Actions manually start ho sake


2. Bot Facebook login kar sake (aapke manually login ke baad)


3. Firefox ya Chrome headless mode na ho (taaki aap manually login kar sakein)




---

📌 .github/workflows/bot.yml File Ka Code

Is file ko update karein aur manually workflow run karein:

name: Run Bot on GitHub Actions (Manual Login via Kiwi Browser)

on:
  workflow_dispatch:  # Manually start karne ke liye

jobs:
  run-bot:
    runs-on: ubuntu-latest  # Linux server pe run karega
    
    steps:
      - name: 🛠️ Checkout Repository
        uses: actions/checkout@v4  # GitHub repo ke code ko fetch karega

      - name: ⚙️ Install Dependencies
        run: |
          sudo apt update && sudo apt install -y firefox wget unzip
          wget https://github.com/mozilla/geckodriver/releases/latest/download/geckodriver-linux64.tar.gz
          tar -xvzf geckodriver-linux64.tar.gz
          sudo mv geckodriver /usr/local/bin/
          pip install -r requirements.txt

      - name: 🚀 Start Bot (Manual Login Required)
        run: python main.py


---

📌 🛠 main.py File Me Manual Login Support

Agar aap manually Facebook me login karna chahte hain, to main.py me ye Chrome ya Firefox ka GUI Mode enable karna hoga:

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def manual_facebook_login():
    """Firefox browser launch karega aur aap manually login kar sakte hain"""
    options = Options()
    options.headless = False  # Headless mode OFF karein taki browser dikh sake

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.facebook.com")

    print("⏳ Please manually login to Facebook... (Waiting for 60 seconds)")
    time.sleep(60)  # Aapko 60 seconds milenge login karne ke liye

    if "home" in driver.current_url:
        print("✅ Facebook login successful!")
        return driver
    else:
        print("❌ Login failed! Please try again.")
        driver.quit()
        return None

if __name__ == "__main__":
    print("🔥 Starting Bot...")
    session = manual_facebook_login()
    if session:
        print("🚀 Bot Started Successfully!")
    else:
        print("❌ Bot Failed to Start.")


---

📌 Kaise Kaam Karega?

1. Kiwi Browser me GitHub pe jaake Actions Tab open karein


2. Manually "Run Workflow" button dabayein


3. Ye GitHub Actions Ubuntu server pe Firefox install karega


4. Aapko manually Facebook me login karne ka option milega (60 sec tak)


5. Login successful hone ke baad bot automatically kaam karega




---

🚀 Extra Notes

Kiwi Browser me Desktop Mode Enable karein!

Headless mode off hai, isliye aap manually login kar sakte hain

Agar Firefox install na ho raha ho, to manually check karein


Koi error aaye to mujhe error ka screenshot bhejein! ✅

