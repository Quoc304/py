import pyautogui, time

for i in range(8,0,-1):
    print(i)
    time.sleep(1)

f = open("a.txt", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
#Tạo bởi Quoc304
#Ngôn ngữ hỗ trợ Python
#3:41:50 ngày 21/8/2022

#Mục đích:Vô dụng vãi ra.
#Kích cỡ:sizeof...#$%.

#Command Line: pip install rickroll
#Thư viện rickroll từ pypi.org #11/7/2017.
#IDE: Vim,Visual Studio Code
