#PYTHON CALCULATOR
intro = input("Type your name: ")
if intro == "Kwadwo" :
    print( "Yo!! U_S_E_L_E_S_S COMRADE! 🤣🤣I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION WHICH YOUR MIND CAN'T CALCULATE😈😈😈😈")
elif intro == "kwadwo":
    print("Yo!! U_S_E_L_E_S_S COMRADE! 🤣🤣I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION  WHICH YOUR MIND CAN'T CALCULATE😈😈😈😈😈😈😈😈")
elif intro == "KWADWO":
    print("Yo!! U_S_E_L_E_S_S COMRADE! 🤣🤣I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION  WHICH YOUR MIND CAN'T CALCULATE😈😈😈😈😈😈😈😈")
elif intro == "Joel":
    print("Yo!! MY ONE AND ONLY BOSS! 🙇🙇‍♂️🔥I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION😈😈😈😈")
elif intro == "JOEL":
    print("Yo!! MY ONE AND ONLY BOSS! 🙇🙇‍♂️🔥I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION😈😈😈😈")
elif intro == "joel":
    print("Yo!! MY ONE AND ONLY BOSS! 🙇🙇‍♂️🔥I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION😈😈😈😈")
elif intro == "ABENA":
    print("heyyy!!BUSH BABYYYYYY ! 👧👧😘🤣I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION😈😈😈😈")
elif intro == "Abena":
    print("heyyy!!BUSH BABYYYYYY ! 👧👧😘🤣I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION😈😈😈😈")
elif intro == "abena":
    print("heyyy!!BUSH BABYYYYYY ! 👧👧😘🤣I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION😈😈😈😈")
else:
    print( "HEYYY! I'M YOUR MINI MATH HELPER FOR SIMPLE MATHS CALCULATION😊✖️➕➖➗")

operator = input("Type an operation (+, - ,*,/): ")
num1 = float(input("Type the 1st number: "))
num2 = float(input("Type the 2nd number: "))

if operator == "+":
    answer = num1 + num2
    print(f"The answer is : {round(answer, 4)} ")
elif operator == "":
    print("Sorry,invalid response. Use either a 'Yes' or a 'No'..")
elif operator == "-":
    answer = num1 - num2
    print(f"The answer is : {round(answer, 4)} ")
elif operator == "*":
    answer = num1 * num2
    print(f"The answer is : {round(answer,4)} ")
elif operator== "/":
    answer = num1 / num2
    print(f"The answer is : {round(answer, 4)} ")
else:
    print (f"{operator} is not valid!")

cont = input("Would you like to use the answer for further calculations?(Yes,No ): ")
if cont == "No":
    print("Alright! Have fun with maths calculations😉 "  )
elif cont == "":
    print("Sorry,invalid response. Use either a 'Yes' or a 'No'..")
elif cont == "Yes":
    operator_2 = input("Type an operation (+, - ,*,/): ")
    num3 = float(input("Type the next number you wanna use: "))
    print(operator_2)
    if operator_2 == "+":
        answer = (num1 + num2) + num3
        print(f"The answer is : {round(answer, 4)} ")
    elif operator_2 == "-":
        answer = (num1 - num2) -  num3
        print(f"The answer is : {round(answer, 4)} ")
    elif operator_2 == "*":
        answer = (num1 * num2) *  num3
        print(f"The answer is : {round(answer, 4)} ")
    elif operator_2 == "/":
        answer = (num1 / num2) /  num3
        print(f"The answer is : {round(answer, 4)} ")

else:
    print("Sorry,invalid response. Use either a 'Yes' or a 'No'..")



