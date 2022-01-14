# Python3 code to demonstrate working of
# Median of list
# Using loop + "~" operator

# initializing list
test_list = [4, 5, 8, 9, 10, 17]

import matplotlib.pyplot as plt

y = ['one', 'two', 'three', 'four', 'five']

# getting values against each value of y
x = [5, 24, 35, 67, 12]
plt.barh(y, x)

# setting label of y-axis
plt.ylabel("pen sold")

# setting label of x-axis
plt.xlabel("price")
plt.title("Horizontal bar graph")
plt.show()