########################################

import os
import re
import sys
import shutil
import requests
from time import sleep
from colorama import Fore
from zipfile import ZipFile
from bs4 import BeautifulSoup

from utilities.Settings.common import *

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET

#########################################

def search_for_updates():
    clear()
    setTitle("New Update Found    |    ")
    r = requests.get("https://github.com/TT-Tutorials/GANG-Nuker/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        Write.Print("\n\n\n          /$$   /$$ /$$$$$$$$ /$$      /$$       /$$   /$$ /$$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$\n", Colors.purple_to_blue, interval=0.000)
        Write.Print("         | $$$ | $$| $$_____/| $$  /$ | $$      | $$  | $$| $$__  $$| $$__  $$ /$$__  $$|__  $$__/| $$_____/\n", Colors.purple_to_blue, interval=0.000)
        Write.Print("         | $$$$| $$| $$      | $$ /$$$| $$      | $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$   | $$   | $$\n", Colors.purple_to_blue, interval=0.000)      
        Write.Print("         | $$ $$ $$| $$$$$   | $$/$$ $$ $$      | $$  | $$| $$$$$$$/| $$  | $$| $$$$$$$$   | $$   | $$$$$\n", Colors.purple_to_blue, interval=0.000)   
        Write.Print("         | $$  $$$$| $$__/   | $$$$_  $$$$      | $$  | $$| $$____/ | $$  | $$| $$__  $$   | $$   | $$__/\n", Colors.purple_to_blue, interval=0.000)   
        Write.Print("         | $$\  $$$| $$      | $$$/ \  $$$      | $$  | $$| $$      | $$  | $$| $$  | $$   | $$   | $$\n", Colors.purple_to_blue, interval=0.000)      
        Write.Print("         | $$ \  $$| $$$$$$$$| $$/   \  $$      |  $$$$$$/| $$      | $$$$$$$/| $$  | $$   | $$   | $$$$$$$$\n", Colors.purple_to_blue, interval=0.000)
        Write.Print("         |__/  \__/|________/|__/     \__/       \______/ |__/      |_______/ |__/  |__/   |__/   |________/\n", Colors.purple_to_blue, interval=0.000)
        print(f'''\n\n                               [{lr}!{w}] GANG-Nuker [{m}{THIS_VERSION}{w}] is OUTDATED''')
        soup = BeautifulSoup(requests.get("https://github.com/TT-Tutorials/GANG-Nuker/releases").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        print(f'                               [\x1b[95m#\x1b[95m\x1B[37m] Would You Like To Update To The Latest Version?')

