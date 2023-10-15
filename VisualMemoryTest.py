from multiprocessing import get_all_start_methods
import pyautogui
import time
import cv2
from pynput.keyboard import Key, Controller
import numpy as np
from PIL import Image


def click(s):
    image = Image.open(r'C:\Users\dk4770\Desktop\screenshot1.png')
    
    # Convert the image to RGB mode
    image = image.convert('RGB')

    # Get the width of the image
    width, height = image.size

    # Initialize a counter for color changes
    size = 0

    for j in range(width-1):
        pixel_color = image.getpixel((j, 0))
        #print(pixel_color)
        if pixel_color != blue and image.getpixel((j+1, 0)) == blue:
            size += 1

    
    
    interval = min(width, height) // (size + 1)

    # Initialize a list to store results
    results = []

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            x = j * interval
            y = i * interval

            # Check if the pixel is white
            pixel_color = image.getpixel((x, y))
            results.append(is_white(pixel_color))
            print(pixel_color)
            if(is_white(pixel_color)): 
                time.sleep(0.5)
                pyautogui.click(763+x, 270+y)
                print("click", x, " ", y)
                time.sleep(0.5)


    print(f"The intersections are white: {results}")
    time.sleep(0.95)
    gameMode()




def is_white(pixel):
    return pixel == (255, 255, 255)

def mse(img1, img2):
    difference = cv2.subtract(img1, img2)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    #print("The images are completely Equal")
        return True
    return False


def gameMode():
    a=1
    while a==1:
        a=2
        s = pyautogui.screenshot(region=(763,270, 380, 380))
        s = cv2.cvtColor(np.array(s), cv2.COLOR_RGB2BGR)
        cv2.imwrite(r'C:\Users\dk4770\Desktop\screenshot1.png', s)
        time.sleep(2)
        click(s);
        




white = (255, 255, 255)
blue = (45, 113, 190)
pyautogui.click(593, 53)
keyboard = Controller()
keyboard.type("https://humanbenchmark.com/tests/memory")
keyboard.press(Key.enter)
keyboard.release(Key.enter)


while True:

    s = pyautogui.screenshot(region=(760,270, 382, 382))
    s = cv2.cvtColor(np.array(s), cv2.COLOR_RGB2BGR)
    cv2.imwrite(r'C:\Users\dk4770\Desktop\screenshot.png', s)
    menu = cv2.imread(r'C:\Users\dk4770\Desktop\menu.png', cv2.IMREAD_COLOR)
    print(mse(menu, s))
    if(mse(menu, s)):
        pyautogui.click(950, 570)
        time.sleep(0.6)
        print("aa")
        gameMode()
        break
        




cv2.destroyAllWindows()



