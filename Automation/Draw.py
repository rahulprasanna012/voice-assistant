import pyautogui
import math
import time

from Base.Mouth import speak


def draw_circle(radius=10, steps=120):


    # Give time for MS Paint to open
    time.sleep(3)

    # Move to the drawing area in Paint
    pyautogui.moveTo(400, 300, duration=1)
    pyautogui.click()

    for step in range(steps):
        angle = 2 * math.pi * step / steps
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        pyautogui.dragRel(x, y, duration=0.01)

    speak("Circle completed!")



def rectangle_spiral():

    pyautogui.moveTo(100, 193, 1)
    pyautogui.rightClick()
    pyautogui.click()
    distance = 300
    while distance > 0:
        pyautogui.dragRel(distance, 0, 0.1, button="left")
    distance = distance - 10
    pyautogui.dragRel(0, distance, 0.1, button="left")
    pyautogui.dragRel(-distance, 0, 0.1, button="left")
    distance = distance - 10
    pyautogui.dragRel(0, -distance, 0.1, button="left")



def draw_logarithmic_spiral(a=1, b=0.2, turns=10):


    # Give time for MS Paint to open
    time.sleep(3)

    # Move to the drawing area in Paint
    pyautogui.moveTo(400, 300, duration=1)
    pyautogui.click()

    for t in range(0, turns * 360, 5):
        angle = math.radians(t)
        r = a * math.exp(b * angle)  # Logarithmic spiral formula
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pyautogui.dragRel(x, y, duration=0.01)

    speak("Logarithmic spiral completed!")
def draw_wave(amplitude=50, wavelength=50, length=500):

    # Give time for MS Paint to open
    time.sleep(3)

    # Move to the drawing area in Paint
    pyautogui.moveTo(100, 400, duration=1)
    pyautogui.click()

    for x in range(0, length, 5):
        y = amplitude * math.sin(2 * math.pi * x / wavelength)
        pyautogui.dragRel(5, y, duration=0.01)

    speak("Wave pattern completed!")
def draw_star(size=200):


    # Give time for MS Paint to open
    time.sleep(3)

    # Move to the drawing area in Paint
    pyautogui.moveTo(400, 300, duration=1)
    pyautogui.click()

    for _ in range(5):
        pyautogui.dragRel(size, 0, duration=0.5)  # Move right
        pyautogui.dragRel(-size // 2, -size, duration=0.5)  # Move up-left
        pyautogui.dragRel(-size // 2, size, duration=0.5)  # Move down-left

    speak("Star completed!")
def draw_zigzag(length=200, height=100, repetitions=5):

    # Give time for MS Paint to open
    time.sleep(3)

    # Move to the drawing area in Paint
    pyautogui.moveTo(100, 200, duration=1)
    pyautogui.click()

    for _ in range(repetitions):
        pyautogui.dragRel(length, height, duration=0.5)  # Move diagonally down-right
        pyautogui.dragRel(-length, height, duration=0.5)  # Move diagonally down-left

    speak("Zigzag pattern completed!")
