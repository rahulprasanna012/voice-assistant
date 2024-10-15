import pyautogui
from Base.Mouth import speak

def move_mouse_up(command):
    print("Moving mouse up...")  # Debugging print
    pixels = extract_number_from_command(command)
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x, current_y - pixels)
    speak(f"Moved mouse {pixels} pixels up.")

def move_mouse_down(command):
    print("Moving mouse down...")  # Debugging print
    pixels = extract_number_from_command(command)
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x, current_y + pixels)
    speak(f"Moved mouse {pixels} pixels down.")

def move_mouse_left(command):
    print("Moving mouse left...")  # Debugging print
    pixels = extract_number_from_command(command)
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x - pixels, current_y)
    speak(f"Moved mouse {pixels} pixels left.")

def move_mouse_right(command):
    print("Moving mouse right...")  # Debugging print
    pixels = extract_number_from_command(command)
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x + pixels, current_y)
    speak(f"Moved mouse {pixels} pixels right.")

def click_mouse(button='left'):
    print(f"Clicking mouse {button}...")  # Debugging print
    pyautogui.click(button=button)
    speak(f"Clicked {button} mouse button.")

def double_click_mouse(button='left'):
    print(f"Double clicking mouse {button}...")  # Debugging print
    pyautogui.doubleClick(button=button)
    speak(f"Double clicked {button} mouse button.")

def drag_mouse(x, y, duration=1, button='left'):
    print(f"Dragging mouse to ({x}, {y})...")  # Debugging print
    pyautogui.dragTo(x, y, duration=duration, button=button)
    speak(f"Dragged mouse to ({x}, {y}) using {button} button.")

def scroll_mouse(clicks=100):
    print(f"Scrolling {clicks} clicks...")  # Debugging print
    pyautogui.scroll(clicks)
    speak(f"Scrolled {clicks} clicks.")

def extract_number_from_command(command):
    print(f"Extracting number from command: {command}")  # Debugging print
    words = command.split()
    for word in words:
        if word.isdigit():
            return int(word)
    return 10  # Default to 10 pixels if no number is mentioned

def extract_coordinates_from_command(command):
    print(f"Extracting coordinates from command: {command}")  # Debugging print
    numbers = [int(s) for s in command.split() if s.isdigit()]
    if len(numbers) >= 2:
        return numbers[0], numbers[1]
    return 0, 0  # Default if no coordinates are provided

def handle_command(command):
    print(f"Handling command: {command}")  # Debugging print
    command = command.lower()

    # Handle movement commands
    if "move mouse up" in command:
        move_mouse_up(command)
    elif "move mouse down" in command:
        move_mouse_down(command)
    elif "move mouse left" in command:
        move_mouse_left(command)
    elif "move mouse right" in command:
        move_mouse_right(command)

    # Handle click commands
    elif "click" in command:
        if "right" in command:
            click_mouse(button='right')
        else:
            click_mouse(button='left')
    elif "double click" in command:
        if "right" in command:
            double_click_mouse(button='right')
        else:
            double_click_mouse(button='left')

    # Handle drag commands
    elif "drag" in command:
        x, y = extract_coordinates_from_command(command)
        drag_mouse(x, y)

    # Handle scroll commands
    elif "scroll up" in command:
        clicks = extract_number_from_command(command)
        scroll_mouse(clicks)
    elif "scroll down" in command:
        clicks = extract_number_from_command(command) * -1
        scroll_mouse(clicks)

    else:
        speak("No valid command detected.")
