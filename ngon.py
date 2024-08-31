from urllib.parse import quote
import datetime
import os
import ssl
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import random
try:
    import base64
    from requests.exceptions import RequestException
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures
    
except ImportError:
    import os
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install concurrent.futures")
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "✯"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1;33m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033[1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]
random_color = random.choice(colors)
def idelay(o):
    while(o>0):
        o=o-1
        print(f"{trang}[{xanhnhat}Đức Phát{trang}] \033[1;33mV\033[1;34mu\033[1;35mi \033[1;32mL\033[1;33mò\033[1;34mn\033[1;35mg \033[1;36mC\033[1;33mh\033[1;34mờ {trang}[\033[1;35m.....""]""["+str(o)+"]""    ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}Đức Phát{trang}] \033[1;31mV\033[1;32mu\033[1;33mi \033[1;34mL\033[1;35mò\033[1;31mn\033[1;32mg \033[1;33mC\033[1;32mh\033[1;35mờ {trang}[\033[1;33m•{trang}....""]"f"{trang}[{xanhnhat}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}Đức Phát{trang}] \033[1;32mV\033[1;33mu\033[1;34mi \033[1;35mL\033[1;36mò\033[1;33mn\033[1;34mg \033[1;35mC\033[1;31mh\033[1;32mờ {trang}[\033[1;35m••{trang}...""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}Đức Phát{trang}] \033[1;31mV\033[1;33mu\033[1;35mi \033[1;33mL\033[1;31mò\033[1;32mn\033[1;34mg \033[1;36mC\033[1;35mh\033[1;31mờ {trang}[\033[1;32m•••{trang}..""]"f"{trang}[{do}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}Đức Phát{trang}] \033[1;32mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;31mn\033[1;35mg \033[1;33mC\033[1;36mh\033[1;35mờ {trang}[\033[1;38m••••{trang}.""]"f"{trang}[{tim}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}Đức Phát{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{vang}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(0.1)
        print(f"{trang}[{xanhnhat}Đức Phát Cte Vailonn{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')

chontool = """ \033[1;31m     _____                       _
\033[1;32m      \_   \_ __ ___  _ __  _   _| |___  ___
\033[1;33m       / /\/ '_ ` _ \| '_ \| | | | / __|/ _ \
\033[1;39m         /\/ /_ | | | | | | |_) | |_| | \__ \  __/
\033[1;35m    \____/ |_| |_| |_| .__/ \__,_|_|___/\___|
\033[1;35m                     |_| 

\033[1;39m┌────────────────── Tool Đức Phát Vipp ──────────────────┐
\033[1;33m ➜ \033[1;39mDEV : Nguyễn Nguyên Đức Phát
\033[1;33m ➜ \033[1;39mFb : Đức Phát ᰔ Shen丨Ctee.com
\033[1;33m ➜ \033[1;39mZalo Support : 0766617331
\033[1;33m ➜ \033[1;39mSupport : Đức Phát ᰔ
\033[1;33m ➜ \033[1;39mBypass : Antiban
\033[1;33m ➜ \033[1;39mTool Spam Ngôn                                          
\033[1;39m└────────────────────────────────────────────────────────┘
\033[1;39m ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻
       	\033[1;31m[\033[1;33m ✯ \033[1;31m] \033[1;34m>\033[1;31m>\033[1;32m> \033[1;39m[ \033[32;5;245m\033[1m\033[38;5;32mĐức Phát Luxury\033[1;38;5;39m ]\033[1;33m: \033[1;32m
\033[1;39m➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻
"""

clear()
runbanner(chontool)
chon = int(input(f"{xanhnhat}Đức Phát Có Cuto Ko 1 có : 2 đéo: {vang}"))
if chon == 1:
    clear()
    runbanner(chontool)
idcanspam=input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập Cái ID Thúi Của Mày Vô :{vang} ')
file_list = []
while True:
    ck=input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Quăng 🍪 Của Mày Vào :{vang} ')
    try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
    except:
        print(f'{do}🍪 sai kìa tk ngu!!')   
runbanner(chontool)
lol = input(f"{xanhnhat}Bạn có muốn spam nhiều nội dung không {trang}({tim}y{vang}/{tim}n{trang}): {vang}")
if lol.lower() == "y":
      stt = 0
      loz = int(input(f"{xanhnhat}Bạn muốn spam bao nhiêu nội dung: "))
      while True:
        stt += 1
        name_files=input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập file chứa nội dung thứ {stt} của bạn (ex: nd.txt) :{vang} ')
        file_list.append(name_files)
        if stt == loz:
          break
elif lol.lower() == "n":
      name_file=input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập file chứa nội dung của bạn (ex: nd.txt) :{vang} ') 
      file_list.append(name_file)
data_list = []
yn=str(input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}bạn muốn spam mãi mãi không :> {trang}({vang}y{trang}/{vang}n{trang}) :{vang} '))
params = {
    "icm": '1',
}
    
headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"247",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
}  
if yn.lower() == 'y':
      delay=int(input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
      while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for selected_file in file_list:
              with open(selected_file, "rb") as file:
                  nds = file.read()
                  #data_list.append(ndss.decode('utf-8'))
            #for ndss in data_list:
              data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nds.decode('utf-8')}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"
              response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
              print(f"\033[1;33mID Sàn Của Con Đú\033[1;97m: {idcanspam} | \033[1;34mĐức Phát (〃ﾟ3ﾟ〃) | \033[1;30mSpam Cho Bạn | \033[1;92mNgôn Spam Của Đấng\033[1;97m: {nds.decode('utf-8')} \033[1;31m| \033[1;31mTool Đức Phátʕっ•ᴥ•ʔっ | \033[1;35mTrạng Thái Spam\033[1;97m: {xanh_la}Thành Công")
              idelay(delay)
        except Exception as e:
          print(f"{do}Nhà Mày Bị Chó Tha Cái Wifi Rồi Kìa=))")
          time.sleep(10)

elif yn.lower() == 'n':
      soluong = int(input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập số tin nhắn muốn gửi :{vang} '))
      delay=int(input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
      for i in range(soluong):
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for name_file in file_list:
              with open(name_file , "rb") as file:
                nds = file.read()
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nds.decode('utf-8')}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"
              response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
              i = i + 1
              print(f"\033[1;31m[\033[1;33m{i}\033[1;31m] \033[1;31m| \033[1;33mID BOX\033[1;97m: {idcanspam} \033[1;31m| \033[1;92mNỘI DUNG\033[1;97m: {nds.decode('utf-8')} \033[1;31m| \033[1;35mTRẠNG THÁI\033[1;97m: {xanh_la}SUCCESS")
              idelay(delay) 
        except Exception as e:
          print(f"{do}Nhà Mày Bị Chó Tha Wifi Kìa🤣")
          time.sleep(10)
else:
    print(f"{do}Vui lòng điền đúng")  