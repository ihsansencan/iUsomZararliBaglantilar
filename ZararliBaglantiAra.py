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
siteAra = input("Aranacak Kelime: ")
zDosyaOku = open(zDosya,mode="r")
zVer = zDosyaOku.readlines()

try:
    for l in zVer:
        if siteAra in l:
            vv = l.split("/")[0].strip("\n")
            print(vv)
            try:
                print("\033[32m"+vv+"\x1b[0m : \033[91m\033[1m"+socket.gethostbyname(vv)+"\x1b[0m")
            except socket.gaierror:
                continue
except KeyboardInterrupt:
    pass