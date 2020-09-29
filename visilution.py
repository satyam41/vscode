import matplotlib.pyplot as plt, numpy as np
city = ['Mumbai', 'Delhi', 'Jabalpur', 'Patna', 'Gaya']
pop = [18400000, 19000000, 1270000, 2050000, 471000]
plt.xlabel("City")
plt.ylabel("Poplution of the City (in cores)")
# plt.plot(city, pop, "r--")
# plt.bar(city, pop, color=['r','k','g', 'b'], width=0.5)
plt.pie(pop, labels=city, autopct="%1.1f%%")
plt.show()