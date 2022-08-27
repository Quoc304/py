import pyautogui
import time

# Variable Delay
#delay = 1 # Test
delay = float(input("Delay Times: "))

#Variable Count
#count_click = 10 # Test
count_click = int(input("Click Times: "))

print("Please move to the position you want to start auto click")

#CountBack.

print("Start...")
for i in range(8,0,-1):
    print(i)
    time.sleep(1)

#X,Y Point.
x, y = pyautogui.position()

#
for _ in range(count_click):
    pyautogui.click(x,y)
    time.sleep(delay)

    





