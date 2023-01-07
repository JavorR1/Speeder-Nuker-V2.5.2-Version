# Coded / Dev / Owner: ††#9999 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022
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
    r = requests.get("https://github.com/JavorR1/Speeder-Nuker-V2.5.1-Official/releases/tag/speeder")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        Write.Print("\n\n\n          /$$   /$$ /$$$$$$$$ /$$      /$$       /$$   /$$ /$$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$\n", Colors.blue_to_cyan, interval=0.000)
        Write.Print("         | $$$ | $$| $$_____/| $$  /$ | $$      | $$  | $$| $$__  $$| $$__  $$ /$$__  $$|__  $$__/| $$_____/\n", Colors.blue_to_cyan, interval=0.000)
        Write.Print("         | $$$$| $$| $$      | $$ /$$$| $$      | $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$   | $$   | $$\n", Colors.blue_to_cyan, interval=0.000)      
        Write.Print("         | $$ $$ $$| $$$$$   | $$/$$ $$ $$      | $$  | $$| $$$$$$$/| $$  | $$| $$$$$$$$   | $$   | $$$$$\n", Colors.blue_to_cyan, interval=0.000)   
        Write.Print("         | $$  $$$$| $$__/   | $$$$_  $$$$      | $$  | $$| $$____/ | $$  | $$| $$__  $$   | $$   | $$__/\n", Colors.blue_to_cyan, interval=0.000)   
        Write.Print("         | $$\  $$$| $$      | $$$/ \  $$$      | $$  | $$| $$      | $$  | $$| $$  | $$   | $$   | $$\n", Colors.blue_to_cyan, interval=0.000)      
        Write.Print("         | $$ \  $$| $$$$$$$$| $$/   \  $$      |  $$$$$$/| $$      | $$$$$$$/| $$  | $$   | $$   | $$$$$$$$\n", Colors.blue_to_cyan, interval=0.000)
        Write.Print("         |__/  \__/|________/|__/     \__/       \______/ |__/      |_______/ |__/  |__/   |__/   |________/\n", Colors.blue_to_cyan, interval=0.000)
        print(f'''\n\n                               [{lr}!{w}] javor-Nuker [{m}{THIS_VERSION}{w}] is OUTDATED''')
        soup = BeautifulSoup(requests.get("https://github.com/JavorR1/Speeder-Nuker-V2.5.1-Official/releases/tag/speeder").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        print(f'                               [\x1b[95m#\x1b[95m\x1B[37m] Would You Like To Update To The Latest Version?')
        choice = input(f'                               [\x1b[95m#\x1b[95m\x1B[37m] (Y/N)?: ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f"\n                               [{g}#{w}] Updating Speeder-Nuker...")

            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("Speeder-Nuker.zip", 'wb')as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("Speeder-Nuker.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Speeder-Nuker.zip")
                cwd = os.getcwd()+'\\Speeder-Nuker\\'
                shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                try:
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), 'Speeder-Nuker.exe')
                except Exception:
                    pass
                shutil.copyfile(cwd+'README.md', 'README.md')                   
                shutil.rmtree('Speeder-Nuker')
                input(f"                               [{g}#{w}] Update Successfully Finished!", end="")
                os.startfile("Speeder-Nuker.exe")
                os._exit(0)

            else:
                new_version_source = requests.get("https://github.com/JavorR1/Speeder-Nuker-V2.5.1-Official/releases/tag/speeder")
                with open("Speeder-Nuker-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Speeder-Nuker-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Speeder-Nuker-main.zip")
                cwd = os.getcwd()+'\\GANG-Nuker-main'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                input(f"                               [{g}!{w}] Update Successfully Finished!")
                print(f'                               [{g}#{w}] Press ENTER to View New Update!')
                if os.path.exists(os.getcwd()+'install.bat'):
                    os.startfile("install.bat")
                elif os.path.exists(os.getcwd()+'start.bat'):
                    os.startfile("start.bat")
                os._exit(0)
