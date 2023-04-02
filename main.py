from machine import ADC
from machine import Pin
import network
import socket
import json
import time
from ir_rx import NEC_16


tuslar = {
    69: 1,
    70: 2,
    71: 3,
    68: 4,
    64: 5,
    67: 6,
    7: 7,
    21: 8,
    9: 9,
    22: '*',
    25: 0,
    13: '#',
    24: '↑',
    8: '←',
    28: 'ok',
    90: '→',
    82: '↓'
    }

def callback(data, addr, ctrl):
    if data > 0:
        dic["tus"] = tuslar[data]


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("SSID", "PASSWORD")
while not wifi.isconnected():
    pass
print(wifi.ifconfig()[0])


host = ''
port = 5560
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, address = s.accept()


temp1 = machine.ADC(4)
led = machine.ADC(26)
pot = machine.ADC(27)
temp = machine.ADC(28)


dic = {"dahiliSicaklik": 0, "parlaklik": 0, "pts": 0, "sicaklik": 0, "tus": 0}

ir = NEC_16(Pin(4, Pin.IN), callback)

while True:
    dic["pts"] = pot.read_u16()
    dic["parlaklik"] = led.read_u16()/65535*100
    dic["sicaklik"] = (temp.read_u16()*(3.3 / 65535))/(100.0 / 1000)
    dic["dahiliSicaklik"] = 27 - ((temp1.read_u16() * (3.3 / 65535))- 0.706) / 0.001721
    veri = json.dumps(dic)
    conn.send(veri.encode())
    time.sleep(1.5)
