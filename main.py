from Function.factory_function import *
from Function.learn_english import learn_english
from Base.Ear import *
from Function.reminder import *
from Function.utils import speak_async
from Generator.big_data import *
from Function.wish import *
from Model.model2 import *
import pywhatkit as kit
from Function.temperature import *
from Function.joke import *
from Function.find_ip import *
from Function.check_net_speed import *
from Automation.scrole_automation import *
from Function.time import *
from Automation.openapp import *
from Automation.mouse import *
from Automation.openwebsite import *
from Generator.codegenerator import *
from Base.Mouth import *
import tkinter as tk
from tkinter import simpledialog
from Data.DLG import *
from Function.intro import intoduction
import random
import threading
import time
import pyautogui

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def jarvis():
    threading.Thread(target=check_reminders, daemon=True).start()
    text = listen().lower()

    if any(keyword in text for keyword in wake_key_word):
        wish()



    while True:

        time.sleep(3)
        text = listen().lower()
        Greating(text)

        command_handled = False

        if 'jarvis are you' in text or 'jarvis get ready' in text:
            speak_async("Hello! I’m here and ready to assist you. Let's make this presentation an amazing one. What can I help you with?")
            command_handled = True

        if "learn english" in text:
            learn_english()  # Enters dedicated function
            continue



        elif 'short into' in text or 'intro' in text:
            intoduction()
            command_handled = True

        elif "temperature" in text:
            speak_async("Checking the temperature")
            Temp()
            command_handled = True

        elif "tell me joke" in text or "joke" in text:
            joke()
            command_handled = True

        elif "time" in text or "what is time" in text:
            what_is_the_time()
            command_handled = True

        elif "internet" in text:
            speak_async("Checking your internet speed")
            get_internet_speed()
            command_handled = True

        elif "ip address" in text:
            speak_async("Finding your IP address")
            ip()
            command_handled = True

        elif "scroll" in text:
            if "up" in text:
                speak_async("Scrolling up")
                scroll_up()
            elif "down" in text:
                speak_async("Scrolling down")
                scroll_down()
            elif "top" in text:
                speak_async("Scrolling to the top")
                scroll_to_top()
            elif "bottom" in text:
                speak_async("Scrolling to the bottom")
                scroll_to_bottom()
            command_handled = True


        elif "send whatsapp message" in text or "send message" in text or "message whatsapp" in text:


            # Create a root window and hide it

            root = tk.Tk()

            root.withdraw()

            # Ask for phone number via dialog box
            speak('On what number should I send the message sir? Please enter in the box: ')


            number = simpledialog.askstring("Input", "On what number should I send the message sir?", parent=root)

            if number:  # Only proceed if user didn't cancel

                speak("What is the message sir?")

                message = listen()

                if message:  # Only proceed if message was provided

                    send_whatsapp_message(number, message)

                    speak("I've sent the message sir.")

            command_handled = True

        elif "open" in text:
            if "website" in text or "site" in text:
                site = text.replace("open", "").replace("website", "").replace("site", "").strip()
                speak_async(f"Opening the website {site}")
                openweb(site)
            elif "code" in text:
                speak_async("Generating code")
                code()
            else:
                app = text.replace("open", "").strip()
                speak_async(f"Opening {app}")
                open(app)
            command_handled = True

        elif "draw" in text:
            handle_drawing_commands(text)
            command_handled = True

        elif "search in google" in text or "search on google" in text:
            query = text.replace("search in google", "").replace("search on google", "").strip()
            speak_async(f"Searching {query} on Google")
            search_google(query)
            command_handled = True

        elif "type" in text or 'write' in text:
            while True:
                content = listen().lower()
                if "exit" in content or "stop" in content:
                    break
                pyautogui.write(content)
            command_handled = True

        elif "deep search" in text:
            speak_async("What should I write?")
            query = listen()
            content = deep_search(query)
            pyautogui.write(content)
            time.sleep(5)
            speak_async(content)
            command_handled = True

        elif "move mouse" in text or "click" in text or "double click" in text or "scroll" in text or "drag" in text:
            handle_command(text)
            command_handled = True
        elif "set reminder" in text or "remind me" in text:
            speak("What should I remind you about?")
            task = listen()
            speak("When should I remind you?")
            time_input = listen()
            remind_time = get_reminder_time(time_input)

            if remind_time:
                add_reminder(task, remind_time)
                speak(f"Reminder set for {task} at {remind_time.strftime('%I:%M %p')}")
            else:
                speak("Sorry, I couldn't understand the time.")
            command_handled = True


        elif any(keyword in text for keyword in bye_key_word):
            speak_async(random.choice(res_bye))
            break

        if not command_handled:
            handle_presentation_commands(text)
            handle_browser_commands(text)
            handle_window_commands(text)
            handle_clipboard_commands(text)
            handle_system_commands(text)

            response = mind(text)
            speak_async(response)

