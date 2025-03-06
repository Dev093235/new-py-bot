import random
import time
from bot.utils import get_random_reply

def auto_reply(message, sender_name):
    """
    Automatically generates a flirty or funny reply based on the received message.
    Uses a predefined list of responses from utils.py.
    """
    reply = get_random_reply(message)
    if sender_name:
        reply = f"{sender_name}, {reply}"
    
    # Simulating typing delay
    time.sleep(random.uniform(1, 3))
    
    return reply

def check_messages(messages):
    """
    Checks new messages and generates auto-replies.
    messages: List of (message, sender_name) tuples.
    """
    replies = []
    for message, sender_name in messages:
        reply = auto_reply(message, sender_name)
        replies.append((sender_name, reply))
    
    return replies
