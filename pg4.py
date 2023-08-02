cimport numpy as np

# Assuming the 'sales_data' NumPy array is already defined with quarterly sales data
# For example, sales_data = np.array([50000, 60000, 75000, 90000])

# Step 1: Calculate the total sales for the year
total_sales_for_year = np.sum(sales_data)

# Step 2: Calculate the percentage increase in sales from the first quarter to the fourth quarter
first_quarter_sales = sales_data[0]
fourth_quarter_sales = sales_data[3]

percentage_increase = ((fourth_quarter_sales - first_quarter_sales) / first_quarter_sales) * 100

# Display the results
print("Total sales for the year:", total_sales_for_year)
print("Percentage increase in sales from the first quarter to the fourth quarter:", percentage_increase, "%")

