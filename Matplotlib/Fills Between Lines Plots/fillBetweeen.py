
# ---------------------------------------------------------
# ------------ fills between line plot --------------------
# fill_between() function in axes module of matplotlib library is used to fill the area between two horizontal curves.

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot')

data = pd.read_csv('data2.csv')

ages = data['Age']
all_dev = data['All_Devs']
python = data['Python']
js = data['JavaScript']

plt.plot(ages, all_dev,  marker='o', linestyle='--', label='All Devs')

plt.plot(ages, python, linestyle='--', label='Python')


plt.fill_between(ages, python, all_dev,  where=(python > all_dev), interpolate=True, alpha=0.25, label='Above Avg')
plt.fill_between(ages, python, all_dev,  where=(python < all_dev), color='k', interpolate=True, alpha=0.25, label='Below Avg')

plt.title('Median Salaries in (USD) By Ages')
plt.xlabel('Ages')
plt.ylabel('Median Salary in (USD)')

plt.legend(loc='upper left')

plt.tight_layout()

plt.show()
