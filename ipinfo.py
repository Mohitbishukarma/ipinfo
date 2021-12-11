import requests
import json
from art import *
tprint("IPInfo",font="universe",chr_ignore=True)

ip=input("\033[1;32m Enter IP : ")
ip_det = requests.get('https://ipinfo.io/'+ip+'/geo')

ip_det=json.loads(ip_det.text)
print(ip_det)




