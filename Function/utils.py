import threading

from Base.Mouth import speak


def speak_async(text):
    threading.Thread(target=speak, args=(text,)).start()
