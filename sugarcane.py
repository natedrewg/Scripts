import keyboard
import time
import pyautogui


def once(i):
  pyautogui.mouseDown(button='left')
  keyboard.press('S')

  sleep('S')
  
  keyboard.release('S')
  keyboard.press('A')

  sleep('A')

  keyboard.release('A')

def check(direction):
      if keyboard.is_pressed('k'):
        keyboard.release('S')
        keyboard.release('A')
        pyautogui.mouseUp(button='left')
        keyboard.wait('k')
        keyboard.press(direction)
        pyautogui.mouseDown(button='left')
      if keyboard.is_pressed('o'):
        keyboard.release('S')
        keyboard.release('A')
        pyautogui.mouseUp(button='left')
        quit()

def stop():
  keyboard.release('S')
  keyboard.release('A')
  pyautogui.mouseUp(button='left')


def sleep(direction):
  for i in range(20):
    time.sleep(1)
    check(direction) 

def main():

  i = 0

  keyboard.wait('o')

  while i < 5:
    once(i)
    i = i + 1
      
  stop()

  print("You went through " + str(i) + " iterations!")
main()
