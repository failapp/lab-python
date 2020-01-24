import time
import sys
import requests
from escpos import *

print("servicio integración ..", time.strftime("Hora: "+"%H:%M"))

# print(sys.argv[1:])
# print("sys -> " + sys.argv[0])

p = printer.Network("192.168.0.192")
p.text("Hello World\n")
p.text("Test impresion ..\n")
p.cut()


'''
# url = "https://ws.architeq.cl/api/v2/locations"
url = "https://ws.architeq.cl/api/v2/users/page/1/size/5"
# args = {} # params ..
headers = {"Content-Type": "application/json", "tenantID": "1013", "tenantKEY": "6e2345df6bfa48ecf56fa071a69757ca"}
# payload = {} # json / data

response = requests.get(url, headers=headers)

if response.status_code == 200:

    print(response.text)

    data = response.json()
    cnt = data["count"]
    print("cnt -> ",  cnt)

    for item in data["users"]:
        print("item -> ", item)
'''









