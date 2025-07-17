# EXERCISE 2: SHOPPING CART PROGRAM

item = input("What item would you like to buy😊😁?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many would you like to buy?: "))

total = float(price * quantity)

print(f"You've bought {quantity} x {item}/s")
print(f"The total will be: ₵{total}")