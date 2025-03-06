import re

def detect_name(message):
    """
    Yeh function message me se naam detect karega.
    Agar naam milega toh return karega, warna None return karega.
    """
    name_pattern = r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)?\b"
    match = re.search(name_pattern, message)
    
    if match:
        return match.group()
    return None

# Testing ke liye
if __name__ == "__main__":
    test_messages = [
        "Hello Mohit, kaise ho?",
        "Bhai Ashu ne kya bola?",
        "Yeh toh sirf ek test hai.",
        "Lazer DJ Meham best hai!"
    ]
    
    for msg in test_messages:
        print(f"Message: {msg} => Name Detected: {detect_name(msg)}")
