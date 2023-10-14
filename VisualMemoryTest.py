
import pyautogui
import time
import cv2
from pynput.keyboard import Key, Controller
import numpy as np



def clickWhitePixels(s):
    xlist = []
    ylist = []
 
    for i in range(s.height-1):
        for j in range(s.width-1):
            if s.getpixel(i,j) == white and s.getpixel(i,j) != white:
                xlist.append(i)
                ylist.append(j)
    



def mse(img1, img2):
    difference = cv2.subtract(img1, img2)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    #print("The images are completely Equal")
        return True
    return False

white = (255, 255, 255)
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
        time.sleep(0.4)
        s = pyautogui.screenshot(region=(760,270, 382, 382))
        


        clickWhitePixels(s);


cv2.destroyAllWindows()




