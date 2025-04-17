import requests

from Base.Mouth import speak


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
def ip():
    response=find_my_ip()
    speak(response)

    return ""