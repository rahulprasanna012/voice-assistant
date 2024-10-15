import pyautogui
# Window controls
def minimize_window():
    pyautogui.hotkey('win', 'down')

def maximize_window():
    pyautogui.hotkey('win', 'up')

def close_window():
    pyautogui.hotkey('alt', 'f4')

def refresh_window():
    pyautogui.hotkey('f5')


# Clipboard and selection
def copy_text():
    pyautogui.hotkey('ctrl', 'c')

def paste_text():
    pyautogui.hotkey('ctrl', 'v')

def cut_text():
    pyautogui.hotkey('ctrl', 'x')

def select_all():
    pyautogui.hotkey('ctrl', 'a')

def hold_shift_select():
    pyautogui.hotkey('shift')


# ------------------- Other System Shortcuts ---------------------

def open_start_menu():
    pyautogui.hotkey('win')

def minimize_all_windows():
    pyautogui.hotkey('win', 'd')

def lock_computer():
    pyautogui.hotkey('win', 'l')

def open_file_explorer():
    pyautogui.hotkey('win', 'e')

def open_task_manager():
    pyautogui.hotkey('ctrl', 'shift', 'esc')

def open_run_dialog():
    pyautogui.hotkey('win', 'r')

def take_screenshot():
    pyautogui.hotkey('win', 'printscreen')