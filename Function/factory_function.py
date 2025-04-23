from Automation.tab_auto import *
from Function.utils import speak_async
from Function.presentation_control import *
from Automation.Draw import *
from Automation.windows import *
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
