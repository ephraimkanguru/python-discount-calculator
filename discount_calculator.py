def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Check if the discount is 20% or more
        discount_amount = price * (discount_percent / 100)  # Calculate the discount amount
        final_price = price - discount_amount  # Subtract the discount from the original price
        return final_price
    else:
        return price  # If discount is less than 20%, return the original price


# Get input from the user
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if final_price == original_price:  # Check if the price was not discounted
    print("No discount applied. The original price is:", original_price)
else:
    print("The final price after discount is:", final_price)
