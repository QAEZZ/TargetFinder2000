import os as o
import json
from urllib.request import urlopen

def osClear():
	rOS = p.system()
	if rOS in ("Windows", "NT"):
		o.system("cls")
	else:
		o.system("clear")

osClear()

print('____________________________________________________________________')
target = input ("  Target IP: ")
print(f'+------------------------------------------------------------------+\n')

apiUrl = "https://ipinfo.io/" + target + "/json"
respone = urlopen(apiUrl)
ZGF0YQ = json.load(respone)

def totalPrint():
  data = ZGF0YQ
  IP = data['ip']
  CITY = data['city']
  STATE = data['region']
  COUNTRY = data['country']
  LATLONG = data['loc']
  ORG = data['org']
  POSTAL = data['postal']
  TZ = data['timezone']

  print( '  ' + IP + '  <--- Internet Protocol (V4) Address \n')
  print( '  ' + CITY + ', ' + STATE + ', ' + COUNTRY + '  <--- Region \n')
  print( '  ' + LATLONG + '  <--- Latitude & Longitude \n')
  print( '  ' + ORG + '  <--- Organization \n')
  print( '  ' + POSTAL + '  <--- Postal (or ZIP) Code \n')
  print( '  ' + TZ + '  <--- Timezone \n')
  print('+------------------------------------------------------------------+')
  print( '\n' + 'GitHub:' + '\n' + 'https://github.com/russian-dev \n')

totalPrint()

programPause = input("Press any key to continue!..")
