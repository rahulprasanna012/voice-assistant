from Function.presentation_control import *
from Base.Ear import *
from Generator.big_data import *
from Function.wish import *
from Model.model2 import *
from Model.model1 import *
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
from Data.DLG import *
from Function.intro import intoduction
import random
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def speak_async(text):

    threading.Thread(target=speak, args=(text,)).start()

def jarvis():
    # Initial greeting
    text = " ".join([word for word in listen().lower().split() if word != 'jarvis'])

    if any(keyword in text for keyword in wake_key_word):
        wish()

    # Main loop
    while True:
        time.sleep(3)
        text = listen().lower()
        Greating(text)

        if 'jarvis are you' in text or 'jarvis get ready' in text:
            speak_async(
                "Hello! I’m here and ready to assist you. Let's make this presentation an amazing one. What can I help you with?")

        elif 'short into' in text or 'intro' in text:

            intoduction()
        elif "start presentation" in text or "start slide show" in text:
            speak_async("Starting the presentation")
            start_presentation()  # Call the function to start the presentation

        elif "next slide" in text or "next" in text:
            speak_async("Moving to the next slide")
            next_slide()  # Call the function to move to the next slide

        elif "previous slide" in text or "previous" in text:
            speak_async("Going to the previous slide")
            previous_slide()  # Call the function to go to the previous slide

        elif "end presentation" in text or "end slideshow" in text:
            speak_async("Ending the presentation")
            end_presentation()  # Call the function to end the presentation

        elif "chat with model" in text or "chat" in text:
            if 'model' in text:
                speak_async("I am model one chatbot.")
                while True:
                    user = listen().lower()
                    if any(keyword in user for keyword in bye_key_word):
                        speak_async(random.choice(res_bye))
                        break
                    response = mind(user)
                    speak_async(response)
            else:
                speak_async("I am model two chatbot.")
                while True:
                    user = listen().lower()
                    if any(keyword in user for keyword in bye_key_word):
                        speak_async(random.choice(res_bye))
                        break
                    response = get_response(user)
                    speak_async(response)

        # Temperature
        elif "temperature" in text:
            speak_async("Checking the temperature")
            Temp()

        # Jokes
        elif "tell me joke" in text or "joke" in text:
            joke()

        # Time
        elif "time" in text or "what is time" in text:
            what_is_the_time()

        # Internet speed
        elif "internet" in text:
            speak_async("Checking your internet speed")
            get_internet_speed()

        # IP Address
        elif "ip address" in text:
            speak_async("Finding your IP address")
            find_my_ip()

        # Scrolling
        elif "scroll up" in text:
            speak_async("Scrolling up")
            scroll_up()
        elif "scroll down" in text:
            speak_async("Scrolling down")
            scroll_down()
        elif "scroll to top" in text:
            speak_async("Scrolling to the top")
            scroll_to_top()
        elif "scroll to bottom" in text:
            speak_async("Scrolling to the bottom")
            scroll_to_bottom()
        elif "send whatsapp message" in text or "send message" in text or "message whatsapp" in text:

            speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")

            speak("What is the message sir?")
            message =listen()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")


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

        # Drawing commands
        elif "draw" in text:
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

        # Google Search
        elif "search in google" in text or "search on google" in text:
            query = text.replace("search in google", "").replace("search on google", "").strip()
            speak_async(f"Searching {query} on Google")
            search_google(query)

        # Browser Control
        elif "close tab" in text:
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

        # Typing and Code Generation
        elif "type" in text or 'write' in text:
            if 'my' in text:
                while True:
                    content = listen().lower()
                    if "exit" in content or "stop" in content:
                        break
                    pyautogui.write(content)
            else:
                speak_async("What should I write?")
                query = listen()
                content = deep_search(query)
                pyautogui.write(content)
                time.sleep(5)
                speak_async(content)

            # Window Management
        elif "minimize window" in text or "minimise window" in text:
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

        # Clipboard and Text Selection
        elif "copy" in text:
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

        # System Shortcuts
        elif "start menu" in text:
            speak_async("Opening the Start menu")
            open_start_menu()

        elif "minimize all" in text or  "minimise all" in text:
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
        # Mouse Control
        elif "move mouse" in text or "click" in text or "double click" in text or "scroll" in text or "drag" in text:
            handle_command(text)

        # Exit commands
        elif any(keyword in text for keyword in bye_key_word):
            speak_async(random.choice(res_bye))
            break


jarvis()
