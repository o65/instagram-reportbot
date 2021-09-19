import requests
import requests.api
from colorama import Fore, Style
import time as sleep 
import time
from time import sleep
from subprocess import run
import os
import subprocess
import platform
import sys
import random
from json import loads
import json

os.system("clear")


s = Fore.RED 
m = Fore.LIGHTMAGENTA_EX
g = Fore.LIGHTGREEN_EX
b = Style.BRIGHT 
w = Fore.WHITE
banner = f"""


{g}{b}▄▄▄  ▄▄▄ . ▄▄▄·      ▄▄▄  ▄▄▄▄▄    ▄▄▄▄·       ▄▄▄▄▄
{g}{b}▀▄ █·▀▄.▀·▐█ ▄█▪     ▀▄ █·•██      ▐█ ▀█▪▪     •██  
{g}{b}▐▀▀▄ ▐▀▀▪▄ ██▀· ▄█▀▄ ▐▀▀▄  ▐█.▪    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
{g}{b}▐█•█▌▐█▄▄▌▐█▪·•▐█▌.▐▌▐█•█▌ ▐█▌·    ██▄▪▐█▐█▌.▐▌ ▐█▌·
{g}{b}.▀  ▀ ▀▀▀ .▀    ▀█▄▀▪.▀  ▀ ▀▀▀     ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 



"""

print(banner)
print(f"""

{w}~ {m}instagram report bot by alex {w}~ 
{b}https://github.com/pausenco
{w}{b}@1_2alexx


""")
time.sleep(2)
os.system("clear")
time.sleep(1)



if platform.system() != "Linux":
    print(Fore.RED + "Linux only!")
    os.system("cls")
    sys.exit(1)


if 'SUDO_UID' not in os.environ.keys():
    print(Fore.RED + "RUN AS ROOT!")
    time.sleep(1)
    os.system("clear")
    sys.exit(1)        

while True:
    try:
        import getpass
        username = input('Username: ')
        password = getpass.getpass("Enter password: ")
        useragents = [
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.1)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/5.0)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4 rv:4.0) Gecko/20190511 Firefox/37.0',
    'Opera/8.24 (X11; Linux i686; sl-SI) Presto/2.11.286 Version/10.00',
    'Opera/9.61 (Windows NT 6.2; en-US) Presto/2.8.291 Version/11.00',
    'Mozilla/5.0 (Windows NT 5.0) AppleWebKit/5360 (KHTML, like Gecko) Chrome/39.0.862.0 Mobile Safari/5360',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_1 rv:5.0; en-US) AppleWebKit/533.24.7 (KHTML, like Gecko) Version/5.0 Safari/533.24.7',
    'Mozilla/5.0 (Windows NT 6.1; en-US; rv:1.9.2.20) Gecko/20140528 Firefox/35.0',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 4.0; Trident/5.1)', ]
        r = requests.session()
        global ig_did, csrftoken, sessionid
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        login_headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '275',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{\"185.88.26.35\": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
            'x-instagram-ajax': '0c15f4d7d44a',
            'x-requested-with': 'XMLHttpRequest'  
        }
        login_data = {
            'username': f'{username}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        login = r.post(login_url, data=login_data, headers=login_headers)
        ig_did = login.cookies['ds_user_id']
        csrftoken = login.cookies['csrftoken']
        sessionid = login.cookies['sessionid']
        u = r.get(f'https://www.instagram.com/{username}/?__a=1')
        idq = str(u.json()['graphql']['user']['id'])

        print(f"logged in > {idq}")
        hed = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '31',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'ig_did={ig_did}; mid=X1ej8wALAAH-iuqPdbS2k838raMR; datr=WVVnXzp0tD7mIRdZ-0jb9JKJ; ig_nrcb=1; shbid=14759; shbts=1612285444.666352; rur=ATN; csrftoken={csrftoken}; ds_user_id={idq}; sessionid={sessionid}',
        'origin': 'https://www.instagram.com',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',  
        'user-agent': random.choice(useragents),
        'x-csrftoken': csrftoken,
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0HH5O9Hioplekd3BZjVgr-KFLmmXjkRtIbTd68b-Ay4U_g',
        'x-instagram-ajax': 'b50ae05deb9f',
        'x-requested-with': 'XMLHttpRequest'
    }

        target = input(Fore.RED + "Enter target: ")
        uss = r.get(f'https://www.instagram.com/{target}/?__a=1')
        idd = str(uss.json()['graphql']['user']['id'])

        print(f"Reporting {target} -> {idd}")

        print(f"""{Fore.RED}Report options
1 -> Spam
2 -> Violence
3 -> Impersonation
4 -> Sexual activity
5 -> Harassment
6 -> Self harm
7 -> Hate speech
""")
        reason_num = int(input('Enter the report reason: '))

        sent = 0
        error = 0
        rs = requests.session()

        if reason_num == 1:
            reports_num = int(input('Amount of reports: '))
            sleeptime = int(input('Sleep time: '))

            for i1 in range(reports_num):
                url1 = f'https://www.instagram.com/users/{idd}/report/'
                data1 = {
                    'source_name': 'profile',  
                    'reason_id': '1'
                }
                report1 = rs.post(url1, data=data1, headers=hed).status_code
                
                if report1 == 200: # If the report went through
                    sent += 1
                
                elif report1 == 400:
                    print(f'{Fore.LIGHTRED_EX}\nRate limited exceeded\n{Fore.WHITE}')
                    os.system('read -s -n 1 -p "\nPress any key to continue..."')
                    print(f'\n{Fore.LIGHTGREEN_EX}Rate limited {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}Waiting 15 minutes{Fore.WHITE}')
                    time.sleep(900)
                    continue

                else:
                    error += 1
                    if error > 10: # If it's counting more then 10 errors -> stop trying so your account won't get banned
                        break
                print(f'{Fore.RED}\rSent: {sent}  Errors: {error}{Fore.WHITE}', end='')
                time.sleep(sleeptime)

        if reason_num == 2: 
            reports_num = int(input('Amount of reports: '))
            sleeptime = int(input('Sleep time: '))

            for i2 in range(reports_num):
                url2 = f'https://www.instagram.com/users/{idd}/report/'
                data2 = {
                    'source_name': 'profile',  
                    'reason_id': '2'
                }
                report2 = rs.post(url2, data=data2, headers=hed).status_code
                
                if report2 == 200: # If the report went through
                    sent += 1
                
                elif report2 == 400:
                    print(f'{Fore.LIGHTRED_EX}\nRate limited exceeded\n{Fore.WHITE}')
                    os.system('read -s -n 1 -p "\nPress any key to continue..."')
                    print(f'\n{Fore.LIGHTGREEN_EX}Rate limited {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}Waiting 15 minutes{Fore.WHITE}')
                    time.sleep(900)
                    continue

                else:
                    error += 1
                    if error > 10:
                        break
                print(f'{Fore.RED}\rSent: {sent}  Errors: {error}{Fore.WHITE}', end='')
                time.sleep(sleeptime)

        if reason_num == 3:
            reports_num = int(input('Amount of reports: '))
            sleeptime = int(input('Sleep time: '))

            for i3 in range(reports_num):
                url3 = f'https://www.instagram.com/users/{idd}/report/'
                data3 = {
                    'source_name': 'profile',  
                    'reason_id': '3'
                }
                report3 = rs.post(url3, data=data3, headers=hed).status_code
                
                if report3 == 200: # If the report went through
                    sent += 1
                
                elif report3 == 400:
                    print(f'{Fore.LIGHTRED_EX}\nRate limited exceeded\n{Fore.WHITE}')
                    os.system('read -s -n 1 -p "\nPress any key to continue..."')
                    print(f'\n{Fore.LIGHTGREEN_EX}Rate limited {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}Waiting 15 minutes{Fore.WHITE}')
                    time.sleep(900)
                    continue

                else:
                    error += 1
                    if error > 10: 
                        break
                print(f'{Fore.RED}\rSent: {sent}  Errors: {error}{Fore.WHITE}', end='')
                time.sleep(sleeptime)

        if reason_num == 4:
            reports_num = int(input('Amount of reports: '))
            sleeptime = int(input('Sleep time: '))

            for i4 in range(reports_num):
                url4 = f'https://www.instagram.com/users/{idd}/report/'
                data4 = {
                    'source_name': 'profile',  
                    'reason_id': '4'
                }
                report4 = rs.post(url4, data=data4, headers=hed).status_code
                
                if report4 == 200: 
                    sent += 1
                
                elif report4 == 400:
                    print(f'{Fore.LIGHTRED_EX}\nRate limited exceeded\n{Fore.WHITE}')
                    os.system('read -s -n 1 -p "\nPress any key to continue..."')
                    print(f'\n{Fore.LIGHTGREEN_EX}Rate limited {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}Waiting 15 minutes{Fore.WHITE}')
                    time.sleep(900)
                    continue

                else:
                    error += 1
                    if error > 10: 
                        break
                print(f'{Fore.RED}\rSent: {sent}  Errors: {error}{Fore.WHITE}', end='')
                time.sleep(sleeptime)

        if reason_num == 5:
            reports_num = int(input('Amount of reports: '))
            sleeptime = int(input('Sleep time: '))

            for i5 in range(reports_num):
                url5 = f'https://www.instagram.com/users/{idd}/report/'
                data5 = {
                    'source_name': 'profile',  
                    'reason_id': '5'
                }
                report5 = rs.post(url5, data=data5, headers=hed).status_code
                
                if report5 == 200: 
                    sent += 1
                
                elif report5 == 400:
                    print(f'{Fore.LIGHTRED_EX}\nRate limited exceeded\n{Fore.WHITE}')
                    os.system('read -s -n 1 -p "\nPress any key to continue..."')
                    print(f'\n{Fore.LIGHTGREEN_EX}Rate limited {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}Waiting 15 minutes{Fore.WHITE}')
                    time.sleep(900)
                    continue

                else:
                    error += 1
                    if error > 10: 
                        break
                print(f'{Fore.RED}\rSent: {sent}  Errors: {error}{Fore.WHITE}', end='')
                time.sleep(sleeptime)

        if reason_num == 6:
            reports_num = int(input('Amount of reports: '))
            sleeptime = int(input('Sleep time: '))

            for i6 in range(reports_num):
                url6 = f'https://www.instagram.com/users/{idd}/report/'
                data6 = {
                    'source_name': 'profile',  
                    'reason_id': '6'
                }
                report6 = rs.post(url6, data=data6, headers=hed).status_code
                
                if report6 == 200: 
                    sent += 1
                
                elif report6 == 400:
                    print(f'{Fore.LIGHTRED_EX}\nRate limited exceeded\n{Fore.WHITE}')
                    os.system('read -s -n 1 -p "\nPress any key to continue..."')
                    print(f'\n{Fore.LIGHTGREEN_EX}Rate limited {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}Waiting 15 minutes{Fore.WHITE}')
                    time.sleep(900)
                    continue

                else:
                    error += 1
                    if error > 10: 
                        break
                print(f'{Fore.RED}\rSent: {sent}  Errors: {error}{Fore.WHITE}', end='')
                time.sleep(sleeptime)

        if reason_num == 7:
            reports_num = int(input('Amount of reports: '))
            sleeptime = int(input('Sleep time: '))

            for i7 in range(reports_num):
                url7 = f'https://www.instagram.com/users/{idd}/report/'
                data7 = {
                    'source_name': 'profile',  
                    'reason_id': '7'
                }
                report7 = rs.post(url7, data=data7, headers=hed).status_code
                
                if report7 == 200: 
                    sent += 1
                
                elif report7 == 400:
                    print(f'{Fore.LIGHTRED_EX}\nRate limited exceeded\n{Fore.WHITE}')
                    os.system('read -s -n 1 -p "\nPress any key to continue..."')
                    print(f'\n{Fore.LIGHTGREEN_EX}Rate limited {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}Waiting 15 minutes{Fore.WHITE}')
                    time.sleep(900)
                    continue

                else:
                    error += 1
                    if error > 10: 
                        break
                print(f'{Fore.RED}\rSent: {sent}  Errors: {error}{Fore.WHITE}', end='')
                time.sleep(sleeptime)

    except ImportError:
            install = input("Failed to load modules! would you like to install? [y/n] ")
            if install.startswith("y"):
                print(Fore.RED + Style.BRIGHT + "Installing.....")
                subprocess.run(["sudo", "bash", "install.sh"]) 
                sys.exit(1)

            elif install.startswith("n"):
                print(Fore.RED + "Exiting")
                time.sleep(1)
                sys.exit(1)

    except KeyboardInterrupt:
        print(Fore.RED + "Exiting...")
        time.sleep(1)
        os.system("clear")
        sys.exit(1)

    except SyntaxError():
        print(Fore.RED + "Use python3 not 2!")
        time.sleep(1)
        os.system("clear")
        sys.exit(1)

    except SyntaxWarning():
        print(Fore.RED + "Use python3 not 2!")
        time.sleep(1)
        os.system("clear")
        sys.exit(1)


