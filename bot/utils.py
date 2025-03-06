import random

# Flirty and fun replies list
REPLIES = [
    "Aree waah! Tumhari baatein toh ekdum 440 volt ki tarah shock deti hain! ⚡😍",
    "Tumhari smile dekh ke toh mera dil Ctrl+S ho gaya! 😉💖",
    "Arre ruk jao, itni taarif sunke toh main blush kar raha hoon! 🙈😆",
    "Tumse baat karke lagta hai ki duniya mein sirf pyaar hi pyaar hai! ❤️😄",
    "Aisa lagta hai tumhari baatein ek romantic Bollywood song ka lyrics hain! 🎶🥰",
    "Kya baat hai, tumhare messages ka notification aate hi dil ekdum fast ho jata hai! 💓📱",
    "Tumhare bina chat toh aise lagti hai jaise DJ bina bass ke! 😜🔊"
]

def get_random_reply(message):
    """
    Returns a random reply from the REPLIES list.
    """
    return random.choice(REPLIES)
