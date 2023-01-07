# Coded / Dev / Owner: JavorR#0001 | https://github.com/JavorR1 | https://github.com/JavorR1
# SPEEDER  / Multi Tool©
# Copyright © 2022/23
########################################


import requests
from colorama import Fore

from utilities.Settings.common import *

def DmDeleter(token, channels):
    for channel in channels:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
            proxies=proxy(),
            headers=getheaders(token))
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted DM: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"\nERROR | {e}")
