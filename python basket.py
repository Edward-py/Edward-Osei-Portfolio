# Define item prices
item_prices = {
    "apple": 1.0,
    "pear": 2.5,
    "orange": 1.6,
}

print("\nWELCOME TO MY SHOP")
print("""\nThese are some items in the shop:
      Apple = £1.00
      Pear = £2.50
      Orange = £1.60""")

# Create an empty basket
basket = {}

while True:
    try:
        budget = float(input("Enter your budget: £"))
        break
    except ValueError:
        print("Wrong data type, please enter a number")

while True:
    try:
        apple_qty = int(input("Enter quantity of apples: "))
        break
    except ValueError:
        print("Wrong data type, please enter an integer")

while True:
    try:
        pear_qty = int(input("Enter quantity of pears: "))
        break
    except ValueError:
        print("Wrong data type, please enter an integer")

while True:
    try:
        orange_qty = int(input("Enter quantity of oranges: "))
        break
    except ValueError:
        print("Wrong data type, please enter an integer")

# Calculate the total cost
total_cost = (item_prices['apple'] * apple_qty) + \
             (item_prices['pear'] * pear_qty) + \
             (item_prices['orange'] * orange_qty)

# Add items and quantities to the basket
basket['apple'] = apple_qty
basket['pear'] = pear_qty
basket['orange'] = orange_qty

# Print items in the basket
print("\nItems in the basket:")
for item in basket:
    print(item, ":", basket[item])


# Check if the user can afford the items
if total_cost > 20:
    discount = total_cost * 0.10  # 10% discount for orders over £20
    total_cost -= discount
    print(f"A discount of £{discount:.2f} has been applied!")

if total_cost <= budget:
    print(f"Success! You can afford the items. Total cost is: £{total_cost:.2f}")
else:
    difference = total_cost - budget
    print(f"You are short by £{difference:.2f}. Your total cost is £{total_cost:.2f}.")

# Buy one get one free offer for pears
if pear_qty >= 2:
    free_pear = pear_qty // 2  
    print(f"You qualify for {free_pear} free pear(s) with the Buy 1 Get 1 Free offer!")
