

import requests
import Base.Mouth
from Base.Mouth import speak


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
def joke():
    response=get_random_joke()
    speak(response)
