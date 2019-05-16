import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv('tips.csv')

data["price_per_person"] = data["total_bill"] / data["size"]

print(data)

print("** People paying more than : **")
print(data[data["price_per_person"] > 10])

print("** Correlation Coefficient between Total Bill and Size of table: **")
print(np.corrcoef(data["total_bill"],data["size"]))

mal = data[data.sex == 'Male']
malTotal = mal['total_bill'].sum()
fem = data[data.sex == 'Female']
femTotal = fem['total_bill'].sum()


x_axis = ['Male', 'Female']
y_axis = [malTotal, femTotal]

ind = np.arange(len(x_axis))

plt.bar(ind, y_axis,color=['blue', 'red'])
plt.ylabel('Total Bills (R)')
plt.xlabel('Sex')
plt.title('Total Bills per Sex')
plt.xticks(ind, x_axis)
plt.show()