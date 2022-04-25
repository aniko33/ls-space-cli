import shutil
import colorama
from colorama import Fore

# Config
# Auto reset color
colorama.init(autoreset=True)
# / = Linux File system, C:\\ = Windows File system
hdd = shutil.disk_usage('/')

# Variable
tz= hdd.total // (2**30)
tza=tz//60
uz=hdd.used//(2**30)
uza=uz//60
fz=hdd.free//(2**30)
fza=fz//60
minspace=tz/5
medspace=tz/2


# Total space and HDD rating
"""
Green: greater than 800 Gigabytes

Yellow: greater than 400 Gigabytes

Red: less than 400 Gigabytes
"""

if tz > 800:
    print(f'Total: {Fore.LIGHTGREEN_EX}{tz}{Fore.RESET} Gigabyte ({Fore.LIGHTGREEN_EX}Good{Fore.RESET})')
elif tz > 400:
    print(f'Total: {Fore.YELLOW}{tz}{Fore.RESET} Gigabyte ({Fore.YELLOW}On average{Fore.RESET})')
elif tz < 400 or tz==400:
    print(f'Total: {Fore.RED}{tz}{Fore.RESET} Gigabyte {Fore.RED}(Bad){Fore.RESET}')


# Free space and used space
if minspace > fz:
    print(f'Used: {Fore.RED}{uz}{Fore.RESET} Gigabyte')
    print(f'Free: {Fore.RED}{fz}{Fore.RESET} Gigabyte')
elif minspace == fz:
    print(f'Used: {Fore.RED}{uz}{Fore.RESET} Gigabyte')
    print(f'Free: {Fore.RED}{fz}{Fore.RESET} Gigabyte')
elif medspace > fz:
    print(f'Used: {Fore.YELLOW}{uz}{Fore.RESET} Gigabyte')
    print(f'Free: {Fore.YELLOW}{fz}{Fore.RESET} Gigabyte')
elif medspace == fz:
    print(f'Used: {Fore.YELLOW}{uz}{Fore.RESET} Gigabyte')
    print(f'Free: {Fore.YELLOW}{fz}{Fore.RESET} Gigabyte')
elif fz > medspace:
    print(f'Used: {Fore.LIGHTGREEN_EX}{uz}{Fore.RESET} Gigabyte')
    print(f'Free: {Fore.LIGHTGREEN_EX}{fz}{Fore.RESET} Gigabyte')