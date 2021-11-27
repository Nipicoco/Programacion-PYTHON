import time
import keyboard
import mouse
 
multiplier = 1  # multiplicador para incrementar el timing
hotKey = 'g'  # triggerea el script.
 
RMB = "right"
keysList = ['a', 's', 'd', 'w', 'q', 'e']
 
delay1 = 0.007   * multiplier
delay2 = 0.06    * multiplier
delay3 = 0.012   * multiplier
delay4 = 0.6     * multiplier
delay5 = 0.15    * multiplier
delay6 = 0.1     * multiplier
 
while True:
    time.sleep(0.01)
    if keyboard.is_pressed(hotKey):
        lastWStat = keyboard.is_pressed('w')
        if keyboard.is_pressed('d'):
            for key in keysList:
                keyboard.release(key)
            time.sleep(delay1)
            mouse.press(RMB)
            time.sleep(delay2)
            mouse.release(RMB)
            time.sleep(delay3)
            keyboard.press('d')
            keyboard.press('w')
            time.sleep(delay1)
            mouse.press(RMB)
            time.sleep(delay3)
            mouse.release(RMB)
            time.sleep(delay3)
            keyboard.release('w')
            keyboard.release('d')
            time.sleep(delay3)
            keyboard.press('s')
            keyboard.press('e')
            time.sleep(delay4)
            keyboard.press('d')
            time.sleep(delay5)
            keyboard.release('d')
            keyboard.release('s')
            time.sleep(delay6)
            keyboard.release('e')
 
            if lastWStat:
                keyboard.press('w')
 
            time.sleep(0.25)
        elif keyboard.is_pressed('a'):
            for key in keysList:
                keyboard.release(key)
            time.sleep(delay1)
            mouse.press(RMB)
            time.sleep(delay2)
            mouse.release(RMB)
            time.sleep(delay3)
            keyboard.press('a')
            keyboard.press('w')
            time.sleep(delay1)
            mouse.press(RMB)
            time.sleep(delay3)
            mouse.release(RMB)
            time.sleep(delay3)
            keyboard.release('w')
            keyboard.release('a')
            time.sleep(delay3)
            keyboard.press('s')
            keyboard.press('q')
            time.sleep(delay4)
            keyboard.press('a')
            time.sleep(delay5)
            keyboard.release('a')
            keyboard.release('s')
            time.sleep(delay6)
            keyboard.release('q')
 
            if lastWStat:
                keyboard.press('w')
 
            time.sleep(0.25)