import csv 
import random
import time
from itertools import count
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import random
import pandas as pd


index = count()
def animate(i):
    data = pd.read_csv('data22.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    
    plt.cla() ## Clear axes
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.legend(loc='upper left')
    plt.tight_layout()
    

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

#data = pd.read_csv('data4.csv')

plt.tight_layout()
plt.show()