#!/usr/bin/env python
import os
import requests
from bs4 import BeautifulSoup
from termcolor import colored
from time import sleep

def main_menu():
    os.system('clear')
    print(colored("contact me : https://wa.me/+916235369260 for any doubts", 'green'))
    with open('banner.txt', 'r') as f:
        banner = f.read()
    print(colored(banner, 'cyan'))

    print(colored("Select the phone number You want\n\n( US NUMBERS )\n\n(1) +14149398617\n(2) +12232407016\n(3) +12066578366\n(4) +12274322496\n(5) +128546971884\n", 'yellow'))

    num = input(":- ")
    if num == '1':
        numone = "+14149398617"
    elif num == '2':
        numone = "+12232407016"
    elif num == '3':
        numone = "+12066578366"
    elif num == '4':
        numone = "+12274322496"
    elif num == '5':
        numone = "+128546971884"
    else:
        print(colored("wrong option", 'red'))
        return

    while True:
        os.system('clear')
        print(colored(f"{numone}  THE INBOX   :any key and enter to refresh.  0 and enter to exit\n\n", 'green'))

        link = requests.get(f"https://sms24.me/en/numbers/{numone}").text
        soup = BeautifulSoup(link, 'html.parser')
        txt = soup.find(class_="placeholder text-break").get_text()

        print(colored(txt, 'magenta'))
        input_key = input("\nPress enter to refresh: ")
        if input_key == '0':
            return
        sleep(2)

if __name__ == '__main__':
    main_menu()
