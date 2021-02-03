#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

print('\033[32m'+"""
***************************
* #UsomZararliBaglantilar *
* @IhsanSencan            *
***************************
"""+'\x1b[0m')

zDosya = "url-list.txt"
with open(zDosya, "r", encoding="latin-1") as f:
    print(f"Toplamda\033[91m\033[1m",f.read().count("\n"),"\033[0madet site bulunuyor.\n")
siteAra = input("Aranacak Kelime: ")
zDosyaOku = open(zDosya,mode="r")
zVer = zDosyaOku.readlines()

try:
    print(25*"*")
    for l in zVer:
        if siteAra in l:
            vv = l.split("/")[0].strip("\n")
            print("\033[33m\033[1m"+vv+"\x1b[0m")
            try:
                print("\033[32m"+vv+"\x1b[0m : \033[91m\033[1m"+socket.gethostbyname(vv)+"\x1b[0m")
            except socket.gaierror:
                continue
except KeyboardInterrupt:
    pass