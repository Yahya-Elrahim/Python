from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices = [60, 40, 30, 80]
labels = ["Java", "C#", "R", "Python"]
# colors = ['blue', 'yellow', 'green', 'red']
explode = [0, 0, 0, 0.1]
plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90,
        wedgeprops={'edgecolor':'black'}, autopct='%1.1f%%')
plt.title('Programming Languages')

plt.show()

