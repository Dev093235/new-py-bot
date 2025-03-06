import os
import random

# Meme folder ka path
MEME_FOLDER = "memes"

def get_random_meme():
    """
    Meme folder se randomly ek meme choose karega aur return karega.
    """
    if not os.path.exists(MEME_FOLDER) or not os.listdir(MEME_FOLDER):
        return "Koi meme nahi mila bhai! 😭"

    meme_list = os.listdir(MEME_FOLDER)
    return os.path.join(MEME_FOLDER, random.choice(meme_list))

# Testing ke liye
if __name__ == "__main__":
    print(get_random_meme())
