import time

from Base.Ear import *
from Generator.big_data import *
from Function.wish import *
from Model.model2 import *
from Model.model1 import *
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
import random
def speak_async(text):
    """Runs the speak function in a separate thread."""
    threading.Thread(target=speak, args=(text,)).start()

def jarvis():
    # Initial greeting
    text = listen().lower()

    if any(keyword in text for keyword in wake_key_word):
        wish()

    # Main loop
    while True:
        time.sleep(3)
        text = listen().lower()
        Greating(text)

        # Chat commands
        if "chat with me" in text or "chat" in text:
            if 'my' in text:
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
        elif "internet speed" in text:
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

        # Opening apps and websites
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
        elif text.endswith("search in google") or text.startswith("search in google") or text.endswith("search on google") or text.startswith("search on google"):
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
        elif "minimize window" in text:
            speak_async("Minimizing the window")
            minimize_window()

        elif "maximize window" in text:
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

        elif "minimize all" in text:
            speak_async("Minimizing all windows")
            minimize_all_windows()

        elif "lock computer" in text:
            lock_computer()
            speak_async("Locking the computer")


        elif "file explorer" in text:
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
