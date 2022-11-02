import keyboard
import time
import pyautogui

#Run through one round of the sugarcane farm
def once(i):
  pyautogui.mouseDown(button='left')
  keyboard.press('S')

  sleep('S')
  
  keyboard.release('S')
  keyboard.press('A')

  sleep('A')

  keyboard.release('A')

#Check if the user is pressing a button to stop the movement of the character
def check(direction):
 #Pressing K will stop the character until you press k again, then the character will start moving again from where it left off
      if keyboard.is_pressed('k'):
        keyboard.release('S')
        keyboard.release('A')
        pyautogui.mouseUp(button='left')
        keyboard.wait('k')
        keyboard.press(direction)
        pyautogui.mouseDown(button='left')
 #Pressing o will stop the character all together and kill the program
      if keyboard.is_pressed('o'):
        keyboard.release('S')
        keyboard.release('A')
        pyautogui.mouseUp(button='left')
        quit()

#This will fully stop all processes on the character
def stop():
  keyboard.release('S')
  keyboard.release('A')
  pyautogui.mouseUp(button='left')

#This function acts as a timer that will allow the character to know when to switch directions
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
