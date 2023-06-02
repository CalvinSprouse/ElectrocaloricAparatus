# imports
import collections

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# this is just used to generate mock live data
import psutil

# define data storing deque
# a deque is kind of like a fixed length list
# values added to the end shove values
# from the front away
cpu = collections.deque(np.zeros(10))
print(f"CPU: {cpu}")

# create a function to update the deque
def update_deque():
    # cpu.popleft()
    cpu.append(psutil.cpu_percent(interval=1))

# function test
update_deque()
print(f"CPU: {cpu}")

# create the figure and define a function to update the figure
fig = plt.figure(figsize=(12,6), facecolor="#DEDEDE")

ax = plt.subplot()



# update function
def update_figure(frame, *fargs):
    # update the deque
    update_deque()

    # clear axis
    ax.cla()

    # label axis
    ax.set_title("CPU Utilization Percent over Time")
    ax.set_xlabel("Time [seconds]")
    ax.set_ylabel("Utilization percent")

    # plot cpu data
    ax.plot(cpu)
    ax.scatter(len(cpu)-1, cpu[-1])
    ax.text(len(cpu)-1, cpu[-1]+2, "{}%".format(cpu[-1]))
    ax.set_ylim(0, 100)

# animate plot
ani = FuncAnimation(fig, update_figure, interval=10)
plt.show()
