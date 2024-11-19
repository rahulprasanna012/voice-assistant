import pyautogui
import math
import time

from Base.Mouth import speak


def draw_circle(radius=10, steps=120):


    # Give time for MS Paint to open
    time.sleep(3)

    # Move to the drawing area in Paint
    pyautogui.moveTo(600, 300, duration=1)
    pyautogui.click()

    for step in range(steps):
        angle = 2 * math.pi * step / steps
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        pyautogui.dragRel(x, y, duration=0.01)

    speak("Circle completed!")



def rectangle_spiral(center_x=600, center_y=400, initial_distance=200, decrement=10):
    """
    Draws a rectangular spiral starting from the center.

    :param center_x: X-coordinate of the center.
    :param center_y: Y-coordinate of the center.
    :param initial_distance: Initial length of the spiral's first side.
    :param decrement: The amount by which each side decreases.
    """
    # Give time for MS Paint to open
    time.sleep(3)

    # Move to the starting position
    pyautogui.moveTo(center_x, center_y, duration=1)
    pyautogui.click()

    distance = initial_distance

    while distance > 0:
        # Move right
        pyautogui.dragRel(distance, 0, duration=0.1, button="left")
        # Move down
        distance -= decrement
        pyautogui.dragRel(0, distance, duration=0.1, button="left")
        # Move left
        distance -= decrement
        pyautogui.dragRel(-distance, 0, duration=0.1, button="left")
        # Move up
        distance -= decrement
        pyautogui.dragRel(0, -distance, duration=0.1, button="left")

    speak("Rectangle spiral completed!")




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
    pyautogui.moveTo(200, 400, duration=1)
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
# def draw_face():
#     """
#     Draws a simple cartoon-style face with eyes, nose, and a smile.
#     """
#     time.sleep(3)  # Give time to open MS Paint
#
#     # Draw the head (circle)
#     draw_circle(center_x=600, center_y=300, radius=100)
#
#     # Draw the left eye
#     draw_circle(center_x=570, center_y=270, radius=10)
#
#     # Draw the right eye
#     draw_circle(center_x=630, center_y=270, radius=10)
#
#     # Draw the nose (a small line)
#     pyautogui.moveTo(600, 300, duration=1)
#     pyautogui.dragRel(0, 20, duration=0.5)
#
#     # Draw the mouth (a semi-circle)
#     center_x, center_y = 600, 340  # Mouth center
#     radius = 40
#     steps = 60
#     prev_x, prev_y = center_x - radius, center_y
#     pyautogui.moveTo(prev_x, prev_y, duration=1)
#     for step in range(1, steps + 1):
#         angle = math.pi * step / steps  # Semi-circle
#         new_x = center_x + radius * math.cos(angle)
#         new_y = center_y + radius * math.sin(angle)
#         pyautogui.dragTo(new_x, new_y, duration=0.01)
#
#
# # Call the draw_face function
# draw_face()