
from matplotlib import pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation

x_values = []
y_values = []

index = count()


def animate(i):
    x_values.append(next(index))
    y_values.append(random.randint(0, 5))

    plt.cla()
    plt.plot(x_values, y_values)



animation_fun = FuncAnimation(plt.gcf(), animate, interval=1000)


plt.tight_layout()
plt.show()
