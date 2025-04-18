import pyttsx3
import threading


def speakbasic(text):
    """Basic text-to-speech function"""
    try:

        print("Jarvis :",text)
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Normal speaking rate
        engine.setProperty('volume', 1.0)  # Full volume
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Default voice


        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Error in speech synthesis: {e}")


def speak(text):
    """Speak the text without animation"""
    # Thread for speech synthesis
    speak_thread = threading.Thread(target=speakbasic, args=(text,))
    speak_thread.start()
    speak_thread.join()  # Wait for speech to finish


