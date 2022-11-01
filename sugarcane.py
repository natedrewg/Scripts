import keyboard
import time
import pyautogui

i = 0

keyboard.wait('o')

while i < 30:
  pyautogui.mouseDown(button='left')
  keyboard.press('S')


  for j in range(21):
    time.sleep(1)
    if keyboard.read_key('k'):
      keyboard.release('S')
      pyautogui.mouseUp(button='left')
      keyboard.wait('k')
      keyboard.press('S')
      pyautogui.mouseDown(button='left')
      j = j + 1
    elif keyboard.read_key('o'):
      keyboard.release('S')
      pyautogui.mouseUp(button='left')
      quit()
    else:
      j = j + 1


  keyboard.release('S')
  keyboard.press('A')


  for k in range(21):
    time.sleep(1)
    if keyboard.read_key('k'):
      keyboard.release('S')
      pyautogui.mouseUp(button='left')
      keyboard.wait('K')
      keyboard.press('A')
      pyautogui.mouseDown(button='left')
    elif keyboard.read_key('o'):
      keyboard.release('S')
      pyautogui.mouseUp(button='left')
      quit()
    else:
      k = k + 1

      
  keyboard.release('A')
  i = i + 1
