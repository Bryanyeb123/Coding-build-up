# EXERCISE 9 : CHECKING SIGN UP FOR LEGAL AGE

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!!!!!🥳🥳🙌😁")
elif age < 0:
    print("Invalid input sign up detail, try again")
elif age < 18:
    print("Sorry😔🥲 you are not eligible to sign up.")
else:
    print("Incorrect details for sign up")

