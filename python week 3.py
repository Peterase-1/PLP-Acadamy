# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount)

# Print result
if discount >= 20:
    print(f"Discount applied. Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Price remains: ${final_price:.2f}")
