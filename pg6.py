# Given item prices and quantities in separate lists
item_prices = [2.5, 3.0, 1.75, 4.5]
item_quantities = [3, 2, 4, 1]

# Given discount rate and tax rate as percentages
discount_rate = 10  # 10% discount
tax_rate = 8  # 8% tax

# Calculate the total cost before any discounts or taxes
total_cost_before_discounts = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))

# Calculate the total discount amount
total_discount_amount = total_cost_before_discounts * (discount_rate / 100)

# Calculate the total cost after applying the discount
total_cost_after_discounts = total_cost_before_discounts - total_discount_amount

# Calculate the total tax amount
total_tax_amount = total_cost_after_discounts * (tax_rate / 100)

# Calculate the final total cost including taxes
final_total_cost = total_cost_after_discounts + total_tax_amount

print("Total Cost before discounts and taxes: $", total_cost_before_discounts)
print("Total Discount Amount: $", total_discount_amount)
print("Total Cost after discounts: $", total_cost_after_discounts)
print("Total Tax Amount: $", total_tax_amount)
print("Final Total Cost including taxes: $", final_total_cost)
