from multiprocessing import get_all_start_methods
import pyautogui
import time
import cv2
from pynput.keyboard import Key, Controller
import numpy as np
from PIL import Image
import keyboard 
import os




# go to the site
pyautogui.click(593, 53)

keyboard = Controller()
keyboard.press(Key.ctrl)
keyboard.press('n')
keyboard.release('n')
keyboard.release(Key.ctrl)
keyboard.type("https://humanbenchmark.com/tests/typing")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
pyautogui.click(600, 53)
time.sleep(1.2)

#save image
s = pyautogui.screenshot(region=(485,415, 945, 130))
s = cv2.cvtColor(np.array(s), cv2.COLOR_RGB2BGR)
cv2.imwrite(r'C:\Users\dk4770\Desktop\screenshot1.png', s)

#go to image to txt
keyboard.press(Key.ctrl)
keyboard.press('t')
keyboard.release('t')
keyboard.release(Key.ctrl)
keyboard.type("https://www.imagetotext.info/")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)


#select the image
pyautogui.click(750, 600)
time.sleep(1)
pyautogui.click(70, 158)
pyautogui.click(550, 170)
pyautogui.click(550, 170)


time.sleep(1)
pyautogui.click(700,800)

#download
time.sleep(10)
pyautogui.click(1210,421)

time.sleep(2)
keyboard.press(Key.ctrl)
keyboard.press('w')
keyboard.release('w')
keyboard.release(Key.ctrl)
time.sleep(0.2)
pyautogui.click(475,427)
pyautogui.click(475,427)
#read file
with open(r'C:\Users\dk4770\Downloads\screenshot.txt') as file:
    while True:
        char = file.read(1)

        if not char:
            print('Reached end of file')
            break
        keyboard.press(char)
        keyboard.release(char)   
        print(char, end="")

os.remove(r'C:\Users\dk4770\Downloads\screenshot.txt')


print("morcha kino")
