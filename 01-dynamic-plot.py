import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
import matplotlib
import time
from collections import deque
matplotlib.use('TkAgg')


def myplot(ax):
    ax.cla()
    ax.plot(x,y)
    ax.set_ylim([-1.1, 1.1])
dt=0.2
datasize=100

# x=deque(np.arange(datasize)*dt, maxlen=datasize)
# y=deque([0]*datasize, maxlen=datasize)
x=deque([], maxlen=datasize)
y=deque([], maxlen=datasize)
fig, ax=plt.subplots()

for i in range(200):
    x.append(dt*i)
    # time1=time.time()
    y.append(np.sin(dt*i))
    myplot(ax)
    plt.pause(0.001)
    # time2=time.time()
    # print(time2-time1)

plt.show()


