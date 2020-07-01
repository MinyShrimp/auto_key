from pynput.keyboard import Listener, Key
from pyautogui import press
from time import sleep
from random import random

__flag = False
__pause = False

def down( key ):
    global __flag, __pause

    if __flag == False and __pause == False:
        if key == Key.space:
            __flag = True
            for _ in range(1, 6):
                press('{}'.format(_))
                sleep( random() / 100 )
        
def up( key ):
    global __flag, __pause

    if key == Key.space:
        __flag = False
    
    if key == Key.home:
        __pause = not __pause
    
    if key == Key.end:
        return False
        
with Listener(on_press=down, on_release=up) as listener:
    listener.join()
