# EXERCISE 9: PYTHON WEIGHT CONVERTER

weight = float(input("Type your weight here⚖️: "))
unit = input("Kilograms or Pounds? (K OR L): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs."

elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not a valid input")

print(f"Your weight is: {round(weight,3)}{unit}")