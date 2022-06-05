import os,time, datetime
from termcolor import colored
from datetime import *
from tkinter import messagebox
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import smtplib
import socket,webbrowser
import time

os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            

def MAİN():
    s = socket.socket()          
    host = "YOUR IP"
    port = 12345                
    try:
        # Bağlantıyı yap
        s.connect((host, port)) 

        # serverden yanıtı al
        yanit = s.recv(1024)
        print(yanit.decode("utf-8"))

        if yanit.decode("utf-8") == "1" or yanit.decode("utf-8") == "KAPAT" or yanit.decode("utf-8") == "Kapat" or yanit.decode("utf-8") == "kapat" or yanit.decode("utf-8") == "shutdown" or yanit.decode("utf-8") == "Shutdown":
            messagebox.showinfo("Alice","Bu bilgisayar M1000 kararı ile kapatılacaktır.")
            os.system("shutdown -p")

        elif yanit.decode("utf-8") == "2" or yanit.decode("utf-8") == "YENİDEN BAŞLAT" or yanit.decode("utf-8") == "Yeniden Başlat" or yanit.decode("utf-8") == "yeniden baslat" or yanit.decode("utf-8") == "restart" or yanit.decode("utf-8") == "Restart":
            messagebox.showinfo("Alice","Bu bilgisayar M1000 kararı ile yeniden başlatılacaktır.")
            os.system("shutdown -r")

        elif yanit.decode("utf-8") == "3" or yanit.decode("utf-8") == "BİLGİ GÖSTER" or yanit.decode("utf-8") == "Bilgi Göster" or yanit.decode("utf-8") == "bilgi göster" or yanit.decode("utf-8") == "show message" or yanit.decode("utf-8") == "Show Message":
            messagebox.showinfo("M1000","SELAM!")
            time.sleep(1)
            MAİN()
        elif yanit.decode("utf-8") == "4" or yanit.decode("utf-8") == "LİNK GÖSTER" or yanit.decode("utf-8") == "Link Göster" or yanit.decode("utf-8") == "link göster" or yanit.decode("utf-8") == "show link" or yanit.decode("utf-8") == "Show Link":
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            time.sleep(1)
            MAİN()

    except socket.error as msg:
        time.sleep(1)
        MAİN()

MAİN()






