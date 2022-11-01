import keyboard
import time
import pyautogui


def once(i):
  pyautogui.mouseDown(button='left')
  keyboard.press('S')

  time.sleep(21)
  
  keyboard.release('S')
  keyboard.press('A')

  time.sleep(21)

  keyboard.release('A')
  i = i + 1


def main():

  i = 0

  keyboard.wait('o')

  while i < 30:
  
    once(i)
      

  print("You went through " + i + "iterations!")
main()
