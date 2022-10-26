#I have used my own google account username and password in another file and
# saved it as credential.py and then imported that file here.
#importing username from credential.py
from credentials import username
#importing password from credential.py
from credentials import password

#importing pyautogui
import pyautogui
# .sleep() with pyautogui suspends execution for given number of seconds
pyautogui.sleep(5)
#to click on address bar
pyautogui.write(['Fn'])

link="https://accounts.google.com/signin"
#.typewrite() function helps to automate the typing of string,
# we just need to pass the string which we want to type.
pyautogui.typewrite(link)
#this will type the link on the address bar when enter will be pressed by user
pyautogui.typewrite('\n')

#after typing it will suspend the program and wait to load the site.
pyautogui.sleep(30)
#this will type the username
pyautogui.typewrite(username)
pyautogui.typewrite('\n')
print("Typing Username")

pyautogui.typewrite(password)
pyautogui.typewrite('\n')
print("Typing Password")
pyautogui.sleep(30)

pyautogui.write(['Fn'])
website = "www.tutorialslink.com"
pyautogui.typewrite(website)
pyautogui.typewrite('\n')
pyautogui.sleep(30)

#thats all about the code