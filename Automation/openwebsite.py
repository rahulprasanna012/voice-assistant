import webbrowser
import random

from Base.Mouth import speak
from Data.DLG import *


def openweb(text):
    for app in text:
        if app.lower() in websites:
            x = random.choice(success_open)
            speak(x + "" + websites[app.lower()])
            webbrowser.open(websites[app.lower()])

        else:
            print(f"Unsupported application: {app}")