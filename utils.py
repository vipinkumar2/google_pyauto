import logging as LOGGER
import subprocess, requests
from faker import Faker
from urllib.parse import urlencode

EMAIL_PASSWORD = 'Noborderz@1234'
BACKUP_EMAIL = 'vipin@noborderz.com'
def run_cmd(cmd, verbose=True):
    """Run shell commands, and return the results

    ``cmd`` should be a string like typing it in shell.
    """
    try:
        if verbose:
            LOGGER.debug(f'Command: {cmd}')

        r = subprocess.run(cmd, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT, shell=True, text=True)

        if verbose:
            if r.returncode == 0:
                LOGGER.debug(f'Successful to run the command: {cmd}')
                LOGGER.debug(f'Result of the command: {r.stdout}')
            else:
                LOGGER.warning(f'Failed to run the command: {cmd}')
                LOGGER.debug(f'Result of the command: {r.stdout}')

        return r.returncode, r.stdout
    except Exception as e:
        LOGGER.error(e)


import time, random
def random_sleep(a=3,b=6):
    random_time = random.randint(a,b)
    LOGGER.info(f'Time sleep for : {random_time}')
    time.sleep(random_time)

def open_fireforx():
    run_cmd('google-chrome')
    
def fake_name():
    fake = Faker()
    name = fake.name()
    name_li = str(name).split(' ')
    fname = name_li[0]
    lname = name_li[-1]
    return name,fname, lname



def get_number(pid='1',country = 'my'):
    while True:
        url = "http://api.getsmscode.com/vndo.php?"

        payload = {
            "action": "getmobile",
            "username": "pay@noborders.net",
            "token": "87269a810f4a59d407d0e0efe58185e6",
            "pid": pid,
            "cocode":country
        }

        payload = urlencode(payload)
        full_url = url + payload
        response = requests.post(url=full_url)
        response = response.content.decode("utf-8")
        if str(response) == 'Message|Capture Max mobile numbers,you max is 5':
            continue
        else:break
    return response

def get_sms(phone_number, pid='1',country = 'my'):
    print('phone_number : ',phone_number)
    url = "http://api.getsmscode.com/vndo.php?"
    payload = {
        "action": "getsms",
        "username": "pay@noborders.net",
        "token": "87269a810f4a59d407d0e0efe58185e6",
        "pid": pid,
        "mobile": phone_number,
        "author": "pay@noborders.net",
        "cocode":country
    }
    payload = urlencode(payload)
    full_url = url + payload
    for x in range(20):
        response = requests.post(url=full_url).text
        if "Google verification" in response:
            response = response.split(' ')
            for i in response : 
                if i.split('-') :
                    i = i.split('—')
                    for i_part in i :
                        try:
                            if int(i_part):
                                return i_part
                        except Exception as e : ...
        time.sleep(10)

    return False

def ban_number(phone_number, pid='1',country = 'my'):
    url = "http://api.getsmscode.com/vndo.php?"
    payload = {
        "action": "addblack",
        "username": "pay@noborders.net",
        "token": "87269a810f4a59d407d0e0efe58185e6",
        "pid": pid,
        "mobile": phone_number,
        "author": "pay@noborders.net",
        "cocode":country
    }
    payload = urlencode(payload)
    full_url = url + payload
    response = requests.post(url=full_url)
    print('response : ',response.text)
    return response