import pyautogui
import time
from pynput.keyboard import Key, Controller


pyautogui.PAUSE = 0.00


def click_pixels(start_x, start_y, end_x, end_y, interval):
    start_time = time.time()
    #print(time.time() - start_time)

    while time.time() - start_time < 5:
        for y in range(start_y, end_y, interval):
            for x in range(start_x, end_x, interval):
                pyautogui.click(x=x, y=y)
                #(x, " " ,y)
                

# Set your adjustable starting and ending pixels
start_x = 600
start_y = 275
end_x = 1450
end_y = 650

# Set the interval (70 pixels apart in this case)
interval = 69

pyautogui.click(1200, 200)

keyboard = Controller()
keyboard.press(Key.ctrl)
keyboard.press('n')
keyboard.release('n')
keyboard.release(Key.ctrl)
keyboard.type("https://humanbenchmark.com/tests/aim")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)

click_pixels(start_x, start_y, end_x, end_y, interval)

exit(0)
