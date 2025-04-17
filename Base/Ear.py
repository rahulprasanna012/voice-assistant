import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Calibrating for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=0.5)

        print("Listening.......", end="", flush=True)

        # Optional settings
        r.pause_threshold = 1.0
        r.phrase_threshold = 0.3
        r.energy_threshold = 4000
        r.dynamic_energy_threshold = True
        r.non_speaking_duration = 0.5

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("\nNo speech detected. Please try again.")
            return ""

    try:
        print("\r", end="", flush=True)
        print("Recognizing......", end="", flush=True)
        query = r.recognize_google(audio, language='en-in')
        print("\r", end="", flush=True)
        print(f"User said : {query}\n")
    except sr.UnknownValueError:
        print("\nCould not understand audio")
        return ""
    except sr.RequestError:
        print("\nCould not request results from Google Speech Recognition service")
        return ""
    return query

# Example usage:
# listen()
