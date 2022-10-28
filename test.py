import pyautogui, random

from utils import BACKUP_EMAIL, EMAIL_PASSWORD, fake_name, get_sms, random_sleep
random_sleep(7,9)




# for _ in range(3):
#     pyautogui.typewrite('\t')
#     pyautogui.sleep(3)
# pyautogui.typewrite('admin@gmail.com')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('0000')
# pyautogui.press('enter')

# --------------------------
pyautogui.press('f6')
pyautogui.typewrite('http://localhost:8000/en/advance/dashboard/youtube_manager/\n')
random_sleep()


# select add account btn
for _ in range(16):
    pyautogui.typewrite('\t')
    pyautogui.sleep(1)
pyautogui.typewrite('\n')
random_sleep()

# select google account
for _ in range(2):
    pyautogui.typewrite('\t')
    pyautogui.sleep(3)
pyautogui.typewrite('\n')
random_sleep()

# select advance option
for _ in range(2):
    pyautogui.typewrite('\t')
    pyautogui.sleep(3)
pyautogui.typewrite('\n')
random_sleep()

for _ in range(3):
    pyautogui.typewrite('\t')
    pyautogui.sleep(3)
pyautogui.typewrite('\n')
random_sleep()

for _ in range(6):
    pyautogui.typewrite('\t')
    pyautogui.sleep(3)
pyautogui.typewrite('\n')
random_sleep()
