import pyttsx3

def speak(text):
    """
    Yeh function text ko Hindi voice me convert karega aur bol ke sunayega.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    # Hindi ya desired voice select karna
    engine.setProperty('voice', voices[0].id)  # Voice select karna (system ke hisaab se change ho sakta hai)
    engine.setProperty('rate', 150)  # Speed adjust karna
    
    engine.say(text)
    engine.runAndWait()

# Testing ke liye
if __name__ == "__main__":
    speak("Namaste! Main tumhara chatbot hoon. Kaise madad kar sakta hoon?")
