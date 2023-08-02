import numpy as np

# Step 1: Import the CSV file into a NumPy array
# Replace 'your_file.csv' with the actual path and filename of your CSV file
# The delimiter parameter specifies the character that separates the values in the CSV file (usually ',' for comma-separated files).
# The skip_header parameter is set to True to skip the header row if it exists.
house_data = np.genfromtxt('C:/Users/divya/AppData/Local/Programs/Python/Python311/FOD PROGRAMS/pg3.csv', delimiter=',', skip_header=True)

# Step 2: Check the structure of the imported data
print("Shape of house_data array:", house_data.shape)

# Step 3: Make sure the column index is correct
# Replace sale_price_column_index with the correct index for the column containing sale prices
print("Column names:", house_data[0])
print("Example row:", house_data[1])

# Step 4: Find the average sale price of houses with more than four bedrooms
bedroom_column_index = 0
sale_price_column_index = 3

# Get the rows where the number of bedrooms is greater than four
houses_with_more_than_four_bedrooms = house_data[house_data[:, bedroom_column_index] > 4]

# Extract the sale prices of those houses
sale_prices_of_houses_with_more_than_four_bedrooms = houses_with_more_than_four_bedrooms[:, sale_price_column_index]

# Calculate the average sale price
average_sale_price = np.mean(sale_prices_of_houses_with_more_than_four_bedrooms)

print("Average sale price of houses with more than four bedrooms:", average_sale_price)
