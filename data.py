"""Datat Visulization"""
"""here we study how to store or represent the data in the form of map.
we import a module name matplotlib.pyplot
their function is .plot for line graph, .bar for bar graph, .barh for horizontal bar graph, .pie for pie graph."""

import matplotlib.pyplot as plt

# Line graph, Bar graph, Horizontal bar graph and Pie graph.

city = ['Jabalpur', 'Mumbai', 'Patna', 'Allahabad']
no = [23,12,11,44]
# plt.plot(city,no, "k", linewidth=3, linestyle=":", marker="*")
# plt.xlabel('City')
# plt.ylabel('Number')
# plt.bar(city, no, color=['r', 'b', 'g', 'k'], width=0.5, bottom=None, align='center')
# plt.barh(city,no, color=['r', 'b', 'g', 'k'])
plt.pie(no, labels=city)
plt.show()