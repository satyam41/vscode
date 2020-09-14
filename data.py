"""Datat Visulization"""
"""here we study how to store or represent the data in the form of map.
we import a module name matplotlib.pyplot
their function is .plot for line graph, .bar for bar graph, .barh for horizontal bar graph, .pie for pie graph.

import matplotlib.pyplot as plt
import numpy as np
# Line graph, Bar graph, Horizontal bar graph and Pie graph.

city = ['Jabalpur', 'Mumbai', 'Patna', 'Allahabad']
no = [23,12,11,44]
on = [32,21,55,40]
plt.plot(city,no,on, "r", linewidth=3, linestyle=":", marker="*")
plt.xlabel('City')
plt.ylabel('Number')
plt.bar(city, no, color=['r', 'b', 'g', 'k'], width=0.5, bottom=None, align='center')
plt.barh(city,no, color=['r', 'b', 'g', 'k'])
plt.pie(no, labels=city, autopct="%1.1f%%")
plt.show()

for i in range(1,11):
    print(i)

arr = np.arange(1,11)
print(arr)
print(type(arr))

arr1 = np.arange(1,11)
arr2 = np.arange(1,11)
plt.plot(arr1, arr2)
np.sin(arr1)
np.cos(arr2)
np.log(arr1)
plt.show()

a = np.linspace(1,20,8)
b = np.arange(1,9)
plt.plot(a,b)
plt.show()
print(a)

a = [2,45,642,3]
b = [2,3,2,3]
plt.plot(a,b, "--", marker="*")
plt.show()"""