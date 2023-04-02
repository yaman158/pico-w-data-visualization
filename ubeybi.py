import socket
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import json
import time

host = '192.168.1.11'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

plt.style.use('fivethirtyeight')
fig = plt.figure()

xa = []
ya = []

xb = []
yb = []

xc = []
yc = []

x4 = []
y4 = []
xd = []
yd = []

a = 0
b = 0
c = 0
d = 0
e = 0

index = count()
sns.set()
ax1 = fig.add_subplot(221)
sns.set()
plt.xlabel("zaman")
plt.ylabel("Dahili Sıcaklık")
plt.title("Dahili Sıcaklık-Zaman Grafiği")

ax2 = fig.add_subplot(222)
sns.set()
plt.xlabel("Zaman")
plt.ylabel("Parlaklık")
plt.title("Parlaklık-Zaman Grafiği")

ax3 = fig.add_subplot(223)
sns.set()
plt.xlabel("Zaman")
plt.ylabel("Potansiyometre")
plt.title("Potansiyometre-Zaman Grafiği")

ax4 = fig.add_subplot(224)
sns.set()
time.time()
def animate(i):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    global y4
    global x4


    mesaj = s.recv(1024)
    veri = json.loads(mesaj)
    sonra = time.time()
    time1 = round(sonra-now,2)
    xa.append(time1)
    xb.append(time1)
    xc.append(time1)
    xd.append(time1)

    ya.append(veri["dahiliSicaklik"])
    yb.append(veri["parlaklik"])
    yc.append(veri["pts"])
    yd.append(veri["sicaklik"])

    if veri["tus"] == 0:
        x1 = xa
        x2 = xb
        x3 = xc
        x4 = xd

        y1 = ya
        y2 = yb
        y3 = yc
        y4 = yd
    elif veri["tus"] == 1:
        x2 = xb
        x3 = xc
        x4 = xd

        y2 = yb
        y3 = yc
        y4 = yd
    elif veri["tus"] == 2:
        x1 = xa
        x3 = xc
        x4 = xd

        y1 = ya
        y3 = yc
        y4 = yd
    elif veri["tus"] == 3:
        x1 = xa
        x2 = xb
        x4 = xd

        y1 = ya
        y2 = yb
        y4 = yd
    elif veri["tus"] == 4:
        x1 = xa
        x2 = xb
        x3 = xc
        x4.pop()
        y1 = ya
        y2 = yb
        y3 = yc
        y4.pop()
    elif veri["tus"] == 5:
        x4.pop()
        y4.pop()
    plt.cla()

    ax1.plot(x1, y1, color = '#444444')

    ax2.plot(x2, y2, color = '#444444')

    ax3.plot(x3, y3, color = '#444444')

    ax4.plot(x4, y4, color = '#444444')


    plt.xlabel("Zaman")
    plt.ylabel("Sıcaklık")
    plt.title("Sıcaklık-Zaman Grafiği")
    i += 1

now = time.time()

ani = FuncAnimation(plt.gcf(), animate, interval=900)


plt.tight_layout()
plt.show()