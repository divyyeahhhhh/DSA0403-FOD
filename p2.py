import numpy as np

# Get sales data from the user as a 3x3 matrix
sales_data = np.array([input("Enter row separated by spaces for product {} sales: ".format(i+1)).split() for i in range(3)], dtype=int)

# Calculate the average price of all products
average_price = np.mean(sales_data)

# Print the result
print("Average price of all products sold in the past month:", average_price)
