#  String operation and Len function
# print("Hello World")
# input("Whats your name ?")
# ------------------------------------------------------------------------------------------------------------------------------------
# Datatypes
# print(type("Crooks"))
# print(type(123))
# print(type(123.455))
# print(type(False))
# ------------------------------------------------------------------------------------------------------------------------------------
# Type conversion
# float()
# int()
# str()
# bool()
# print("Number of letters in your name: " + str(len(input("Enter your name"))))
# ------------------------------------------------------------------------------------------------------------------------------------
# Mathematical Operators +, -, *, /, // and **
# PEMDAS - Parentheses (), Exponents **, Multiplication/Division *,/,// , Addition/Subtraction +,-
# Left to Right operations
# print(3 ** 3 - 3 * 3 - 3)
# ------------------------------------------------------------------------------------------------------------------------------------
# Number Manupulation
# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(round(bmi))
# print(round(bmi, 2))
# ------------------------------------------------------------------------------------------------------------------------------------
# Assignment operators +=, -=, *=, /=, //=, **=
# ------------------------------------------------------------------------------------------------------------------------------------
# f string - f"{}"
# bmi = 84 / 1.65 ** 2
# print(f"Your BMI is {bmi: .2f} and is in the {bmi: .2f} category.")
# ------------------------------------------------------------------------------------------------------------------------------------
# Modulo Operator %
# number = int(input("What's your favorate number? "))
# if(number % 2 == 0):
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")
# ------------------------------------------------------------------------------------------------------------------------------------
#If-Else & Elif ladder
# height =int( input("What is your height ?"))
# if(height>120):
#     print("Your are allowed to ride")
#     age = int(input("Whats your age ?"))
#     if(age<12):
#         print("Please pay Rs. 20")
#     elif (age<18):
#         print("Please pay Rs. 30")
#     else:
#         print("Please pay Rs. 50")
# else:
#     print("You are not allowed")
# print("Enjoy ride !!!")
# ------------------------------------------------------------------------------------------------------------------------------------
#Random Module
# import rand   om
# random_integer = random.randint(1,3)
# print(random_integer)
# ------------------------------------------------------------------------------------------------------------------------------------
# random_num_1_5 = random.random() * 10
# print(random_num_1_5)
# ------------------------------------------------------------------------------------------------------------------------------------
# random_float = random.uniform(1,3)
# print(random_float)
# ------------------------------------------------------------------------------------------------------------------------------------
# Head & Tail coin flip
# coin_flip = random.randint(0,1)
# if(coin_flip == 1):
#     print("HEADS")
# else:
#     print("TAILS")
# ------------------------------------------------------------------------------------------------------------------------------------
# Loop
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
# ------------------------------------------------------------------------------------------------------------------------------------
# Range function : This code doesn't do anything by itself. For example, if you tried to print it, it would not give you individual numbers.
# range(1,10) 