# ------------------------------------------------------------------------------
# ------------------------ Histogram  ------------------------------------------
# A histogram is basically used to represent data provided in a form of
# some groups.It is accurate method for the graphical representation of numerical data distribution.It is a type of
# bar plot where X-axis represents the bin ranges while Y-axis gives information about frequency.

from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('ggplot')

data = pd.read_csv('data.csv')
data2 = pd.read_csv('data2.csv')

ids = data['Responder_id']
ages = data2['Age']
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages,color='b', edgecolor='black')

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
