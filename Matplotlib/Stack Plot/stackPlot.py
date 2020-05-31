# ----------------------------------------------------------
# --------------------- Stack Plots ------------------------

# Stackplot is used to draw a stacked area plot. It displays the complete data for
# visualization. It shows each part stacked onto one another and how each part makes the complete figure. It displays
# various constituents of data and it behaves like a pie chart. It has x-label, y-label and title in which various
# parts can be represented by different colors.

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

# Colors in hex decimal format for Stack Plot
colors = ['#6d904f', '#fc4f30', '#008fd5']

labels = ['PlayerOne', 'PlayerTow', 'PlayerThree']


plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

# lower left, lower left, upper right, upper left, lower center, upper center
plt.legend(loc=(0.07, 0.05))

plt.title("Stack Plot")

plt.tight_layout()

plt.show()
