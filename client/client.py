import json
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import socket as sk

fig, [ax1, ax2] = plt.subplots(2, sharex=True)

x = []
y1 = []
y2 = []

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

sock.setblocking(False)
sock.bind(('127.0.0.1', 8081))

def animate(i, x, y1, y2):

    try:
        data = sock.recv(10).decode('utf8').split(',')
    except Exception as e:
        return

    print(data)

    x.append(dt.datetime.now())

    y1.append(int(data[1]))
    y2.append(int(data[0]))

    x = x[-60:]
    y1 = y1[-60:]
    y2 = y2[-60:]

    ax1.clear()
    ax2.clear()

    ax1.set_title('Number of Vehicles')
    ax2.set_title('Number of Pedestrians')
    ax2.set_xlabel('Time')

    ax1.plot(x, y1)
    ax2.plot(x, y2, color='orange')

ani = animation.FuncAnimation(fig, animate, fargs=(x, y1, y2), interval=500)

plt.show()
