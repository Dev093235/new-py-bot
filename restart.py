import os
import sys
import time

def restart_program():
    print("🔄 Restarting bot...")
    time.sleep(2)
    os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    restart_program()
