
import pyautogui


import asyncio
import warnings

# Set event loop policy to avoid the warning
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Suppress the specific warning (optional)
warnings.filterwarnings("ignore", category=RuntimeWarning, message="Proactor event loop does not implement add_reader")

# Function to start the presentation
def start_presentation():
    pyautogui.hotkey('alt', 'f5')  # Start the slideshow in PowerPoint
    print("Starting the presentation")

# Function to go to the next slide
def next_slide():
    pyautogui.press('right')  # Move to the next slide
    print("Moving to the next slide")

# Function to go to the previous slide
def previous_slide():
    pyautogui.press('left')  # Move to the previous slide
    print("Going to the previous slide")

# Function to end the presentation
def end_presentation():
    pyautogui.press('esc')  # End the slideshow
    print("Ending the presentation")



