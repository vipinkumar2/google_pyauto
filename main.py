from ctypes.wintypes import PULARGE_INTEGER
import logging
import random
import subprocess, threading
from utils import BACKUP_EMAIL, EMAIL_PASSWORD, fake_name, get_number, get_sms, random_sleep, open_fireforx
import pyautogui

threading.Thread(target=open_fireforx).start()

random_sleep()

link="https://accounts.google.com/signin"


pyautogui.keyDown('shift')
pyautogui.typewrite('\t\t\n')
pyautogui.keyUp('shift')
random_sleep()
pyautogui.typewrite('https://accounts.google.com/signup')
random_sleep()

pyautogui.press('enter')
# pyautogui.typewrite('\t\t\n')

random_sleep()

name, fname, lname = fake_name()
username = str(fname)+str(lname)+str(random.randint(10000,99999))
print(username)
pyautogui.typewrite(str(fname)+'\t'+str(lname)+'\t'+username+'\t\t'+EMAIL_PASSWORD+'\t'+EMAIL_PASSWORD+'\t\t\n')

random_sleep()
new_number = get_number()
random_sleep()

for i in range(5):
    pyautogui.typewrite('\t')
    pyautogui.sleep(3)
pyautogui.typewrite(f'+{new_number}\t\n')

# input('EWnter 3')
random_sleep()
number_otp = get_sms(new_number)
pyautogui.typewrite(str(number_otp)+'\t\n')

random_sleep()
month_first_li =  ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

BIRTHDATE = str(random.randint(2,28))
BIRTH_MONTH = random.choice(month_first_li)
BIRTH_YEAR = str(random.randint(1985,2003))
for _ in range(6):
    pyautogui.typewrite('\t')
    pyautogui.sleep(3)
pyautogui.typewrite(BACKUP_EMAIL+'\t')
pyautogui.typewrite(BIRTHDATE+'\t')
pyautogui.typewrite(BIRTH_MONTH+'\t')
pyautogui.typewrite(BIRTH_YEAR+'\t')
pyautogui.typewrite('r\t\t\n')

for _ in range(7):
    pyautogui.typewrite('\t')
    pyautogui.sleep(3)
pyautogui.typewrite('\n')

for _ in range(9):
    pyautogui.typewrite('\t')
    pyautogui.sleep(3)
pyautogui.typewrite('\n')


random_sleep(10,15)
pyautogui.press('f6')
pyautogui.typewrite('https://www.youtube.com/')
random_sleep()
pyautogui.press('f5')


input('Enter :')



pyautogui.typewrite('\n')
