import pyautogui
import time

x = 300
y = 600

while True:
	pyautogui.moveTo(x,y,0.1)
	x,y = y,x
	pyautogui.moveTo(x,y,0.1)
	x,y = y,x
	pyautogui.moveTo(x,y,0.1)
	x,y = y,x
	pyautogui.typewrite(["ctrlleft"])
	time.sleep(240)
