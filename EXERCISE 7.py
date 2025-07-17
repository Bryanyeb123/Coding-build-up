#  EXERCISE 7 FINDING THE HYPOTENEUS OF A TRIANGLE
import math
a = float(input("Type in the opposite side: "))
b = float(input("Type in the adjacent side: "))

hypotenuse = math.sqrt((pow(a, 2)) + (pow(b,2)))

print(f"The hypotenuse will be : {round(hypotenuse,2)}cm 🔥")