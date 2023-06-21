import numpy as np
import matplotlib.pyplot as plt
import csv


f = open('numbers.csv', 'r')
d= open('data.csv', 'r')
array_numbers = csv.reader(f)
array_data = csv.reader(d)
x_tmp = []
y_tmp = []
for row in array_numbers:
    try:
        for n in range(0, 51):
            x_tmp.append(float(row[n]))
    except:
        pass

for row in array_data:
    try:

        for n in range(0, 50):
            y_tmp.append(float(row[n]))

    except:
        pass

print(len(x_tmp))
print(len(y_tmp))
x_train = np.array(x_tmp)
y_train = np.array(y_tmp)
w = 2 #weight parameter
b = 7 #bias parameter

print(f"{x_train}")
print(f"{y_train}")

 #m equals to the amount of training examples


# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.legend()
plt.show()

