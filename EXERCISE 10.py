# EXERCISE 10: TEMPERATURE CONVERSION PROGRAM

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Type the temperature here🌡️:  "))

if unit == "C":
    temp = round(((temp * (9/5)) +32),1)
    print(f"The temperature in Fahrenheit will be: {temp}°F")
elif unit == "F":
    temp = round(((temp - 32)* 5/9),1)
    print(f"The temperature in Celsius will be: {temp}°C")
else:
    print(f"{unit} is an incorrect temperature measurement")