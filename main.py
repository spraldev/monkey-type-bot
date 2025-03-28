from PIL import ImageGrab
import pytesseract
import os
import time
from pyautogui import typewrite

time.sleep(5)

def first():
    l1bbox = (194, 499, 1499, 578)
    l1screenshot = ImageGrab.grab(bbox=l1bbox)
    l1 = pytesseract.image_to_string(l1screenshot)

    l2bbox = (194, 587, 1510, 646)
    l2screenshot = ImageGrab.grab(bbox=l2bbox)
    l2 = pytesseract.image_to_string(l2screenshot)

    l3bbox = (192, 643, 1498, 716)
    l3screenshot = ImageGrab.grab(bbox=l3bbox)
    l3 = pytesseract.image_to_string(l3screenshot)

    typewrite(l1)
    typewrite(" ")
    typewrite(l2)
    typewrite(" ")
    typewrite(l3)
    typewrite(" ")

def second():
    l2bbox = (194, 587, 1510, 646)
    l2screenshot = ImageGrab.grab(bbox=l2bbox)
    l2 = pytesseract.image_to_string(l2screenshot)

    typewrite(l2)
    typewrite(" ")

first()

while True:
    second()
