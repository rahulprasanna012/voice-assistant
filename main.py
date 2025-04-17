from Function.presentation_control import *
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
from Automation.Draw import *
from Automation.mouse import *
from Automation.tab_auto import *
from Automation.openwebsite import *
from Generator.codegenerator import *
from Automation.windows import *
from Base.Mouth import *
from Function.reminder import check_reminders

from Data.DLG import *
from Function.intro import intoduction
import random
import threading
import time
import pyautogui

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def handle_presentation_commands(text):
    if "start presentation" in text or "start slide show" in text:
        speak_async("Starting the presentation")
        start_presentation()
    elif "next slide" in text or "next" in text:
        speak_async("Moving to the next slide")
        next_slide()
    elif "previous slide" in text or "previous" in text:
        speak_async("Going to the previous slide")
        previous_slide()
    elif "end presentation" in text or "end slideshow" in text:
        speak_async("Ending the presentation")
        end_presentation()

def handle_drawing_commands(text):
    if "circle" in text:
        speak_async("Drawing a circle")
        draw_circle()
    elif "rectangle spiral" in text:
        speak_async("Drawing a rectangle spiral")
        rectangle_spiral()
    elif "logarithmic spiral" in text:
        speak_async("Drawing a logarithmic spiral")
        draw_logarithmic_spiral()
    elif "wave" in text:
        speak_async("Drawing a wave")
        draw_wave()
    elif "star" in text:
        speak_async("Drawing a star")
        draw_star()
    elif "zigzag" in text:
        speak_async("Drawing a zigzag")
        draw_zigzag()

def handle_browser_commands(text):
    if "close tab" in text:
        speak_async("Closing the current tab")
        close_tab()
    elif "open browser menu" in text:
        open_browser_menu()
    elif "zoom in" in text:
        zoom_in()
    elif "zoom out" in text:
        zoom_out()
    elif "refresh page" in text:
        refresh_page()
    elif "switch to next tab" in text:
        switch_to_next_tab()
    elif "switch to previous tab" in text:
        switch_to_previous_tab()
    elif "open history" in text:
        open_history()
    elif "open bookmarks" in text:
        open_bookmarks()
    elif "go back" in text:
        go_back()
    elif "go forward" in text:
        go_forward()
    elif "dev tools" in text:
        open_dev_tools()
    elif "toggle full screen" in text:
        toggle_full_screen()
    elif "private window" in text:
        open_private_window()
    elif "new tab" in text:
        open_new_tab()

def handle_window_commands(text):
    if "minimize window" in text or "minimise window" in text:
        speak_async("Minimizing the window")
        minimize_window()
    elif "maximize window" in text or "maximise window" in text:
        speak_async("Maximizing the window")
        maximize_window()
    elif "close window" in text:
        speak_async("Closing the window")
        close_window()
    elif "refresh window" in text:
        speak_async("Refreshing the window")
        refresh_window()

def handle_clipboard_commands(text):
    if "copy" in text:
        speak_async("Copying the selected text")
        copy_text()
    elif "paste" in text:
        speak_async("Pasting the text")
        paste_text()
    elif "cut" in text:
        speak_async("Cutting the selected text")
        cut_text()
    elif "select all" in text:
        speak_async("Selecting all text")
        select_all()
    elif "hold shift" in text:
        speak_async("Holding shift for selection")
        hold_shift_select()

def handle_system_commands(text):
    if "start menu" in text:
        speak_async("Opening the Start menu")
        open_start_menu()
    elif "minimize all" in text or "minimise all" in text:
        speak_async("Minimizing all windows")
        minimize_all_windows()
    elif "lock computer" in text:
        lock_computer()
        speak_async("Locking the computer")
    elif "file explorer" in text or "open file" in text:
        open_file_explorer()
        speak_async("Opening File Explorer")
    elif "task manager" in text:
        speak_async("Opening Task Manager")
        open_task_manager()
    elif "run dialog" in text:
        speak_async("Opening the Run dialog")
        open_run_dialog()
    elif "screenshot" in text:
        speak_async("Taking a screenshot")
        take_screenshot()

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
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = listen()
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
            if handle_presentation_commands(text): return
            if handle_browser_commands(text): return
            if handle_window_commands(text): return
            if handle_clipboard_commands(text): return
            if handle_system_commands(text): return
            response = mind(text)
            speak_async(response)

jarvis()