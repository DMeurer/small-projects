import pyautogui
import time
import keyboard
import win32api, win32con

# counting variable
x=0

# click on a specific position
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep (0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# send message
def Message():
    Message = "Ter text den man senden will"
    encoded = list(Message)
    for i in encoded: 
        keyboard.press(i)
        keyboard.release(i) 

# main loop
while keyboard.is_pressed('c') == False: 

    # wait for specific pixel to turn green
    if pyautogui.pixel(315,188)[0]== 6:
    
        # send message
        click(297,255)
        time.sleep(1)
        Message()
        time.sleep(1)
        click(958,1007)
        click(172,304)
        time.sleep(1)
        Message()
        time.sleep(1)
        click(958,1007)
        x=x+1
        raise SystemExit
print(x)