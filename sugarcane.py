import keyboard
import time
import pyautogui


def once(i):
  pyautogui.mouseDown(button='left')
  keyboard.press('S')

  sleep()
  
  keyboard.release('S')
  keyboard.press('A')

  sleep()

  keyboard.release('A')
  i = i + 1

def stop():
      if keyboard.is_pressed('k'):
        keyboard.release('S')
        keyboard.release('A')
        pyautogui.mouseUp(button='left')
        keyboard.wait('k')
        


def sleep():
  for i in range(42):
    time.sleep(.5)
    stop()



def main():

  i = 0

  keyboard.wait('o')

  while i < 500:
    once(i)
      

  print("You went through " + i + "iterations!")
main()
