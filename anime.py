from itertools import count
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import random

#plt.style.use('fivethirtyeight')
x_vals = []
y_vals = []

#plt.plot(x_vals, y_vals)

index = count()
def animate(i):
    x_vals.append(next(index))
    print ('animate')
    y_vals.append(random.randint(0,5))
    plt.cla()
    plt.plot(x_vals, y_vals)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

#data = pd.read_csv('data4.csv')

plt.tight_layout()
plt.show()