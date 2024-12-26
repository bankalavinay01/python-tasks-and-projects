#coding exercise
# #exercise-1
# ''' 
# Vowel Checker:Write a Python program that takes a character as input and checks whether 
# it is a vowel or not. Use the if-else statement.
# '''
# English_Letter = input("Enter the letter : ")
# if English_Letter in "aeiouAEIOU":
#     print(f"The Letter you entered is Vowel")
# else : print(f"The Letter you entered is Consonants")

# exercise-2
# '''
# Age Group Classification :
# Write a program that takes an age as input and classifies the person into one of the following age groups:
#  Child: 0 -12 years
#  Teenager: 13 -17 years
#  Adult: 18 - 64 years
#  Senior: 65 years and older
#  '''
# Age_Category = int(input("Enter age:"))
# if Age_Category >=65 :
#     print(f"You are Senior citizen as your age is {Age_Category}")
# elif Age_Category >=18 :
#     print(f"You are Adult as your age is {Age_Category}")
# elif Age_Category >=13 :
#     print(f"You are Teenager as your age is {Age_Category}")
# else:
#     print(f"You are Child as your age is {Age_Category}")

#exercise-3
# '''
# Number Classifier: Write a program that takes an integer as input and classifies it as positive, 
# negative, or zero. Use the if-elif-else statement
# '''
# Enter_Number = int(input("enter number :"))
# if Enter_Number >= 1 :
#     print(f"number you enter is {Enter_Number} and it is positive number")
# elif Enter_Number <=-1 :
#     print(f"number you enter is {Enter_Number} and it is negative number")
# else :
#     print(f"number you enter is {Enter_Number} and it is Zero Value")

    #exercise-4
# '''
# Leap Year Checker: Create a program that checks whether a given year is a leap year or not. A 
# leap year is divisible by 4, but not by 100 unless it is divisible by 400.
# '''
# Year_Check = int(input("Enter Year : "))
# if (Year_Check %4 == 0 and Year_Check % 100 !=0) or (Year_Check %400 ==0):
#     print(f"year you enter {Year_Check} is Leap Year")
# else : print(f"year you entered {Year_Check} is Normal Year")

#exercise-5
# '''
# Calculator: Build a simple calculator program that takes two numbers and an operator 
# (+, -, *, /) as input and performs the corresponding operation
# '''
# Value_1 = int(input("Enter Value 1 : "))
# Value_2 = int(input("Enter Value 2 : "))
# Operation = input("Enter operator ")
# if Operation== "+":
#     print(f"Add the {Value_1} with {Value_2} and Sum of two numbers is {Value_1 + Value_2}")
# elif Operation == "-":
#     print(f"Subtract the {Value_1} with {Value_2} and Result is {Value_1 - Value_2}")
# elif Operation == "*":
#     print(f"Multiply the {Value_1} with {Value_2} and Result is {Value_1 * Value_2}")
# elif Operation == "%":
#     print(f"Modulus the {Value_1} with {Value_2} and Result is {Value_1 % Value_2}")
# else :print("Entered incorrect Operator")

#exercise-6
# '''
# Short Hand If: Rewrite the following code using the short-hand 
# if statement
# x = 8
# if x % 2 == 0: result = "Even"
# else: result = "Odd
# '''

# X = int(input("Enter the value X :"))
# print(" X is Even") if X %2== 0 else print(" X is Odd")


# #exercise-7
# '''
# Discount Calculator:Create a program that calculates the final price after applying a discount. 
# The program should take the original price and the discount percentage as input.
# '''
# Product_Price = int(input(" Produce MRP is :"))
# Discount_Percent= int(input(" Enter Discount % : "))
# Discount_Amount = Product_Price * (Discount_Percent/100)
# Final_Price = Product_Price - Discount_Amount
# print(f" The Product Price is {Product_Price} and the Discount % is {Discount_Percent} and Now the Final price is {Final_Price} ")


#exercise-8
# '''
# BMI Calculator:
#  Write a program that calculates the Body Mass Index (BMI) using the 
# formula: BMI = weight (kg) / (height (m))^2. The program should take 
# weight and height as input
# '''
# Body_Weight = int(input("Please enter your Weight :"))
# Body_Height = float(input("Enter your Hight :"))
# BMI_Cal = Body_Weight/(Body_Height)**2
# print(f"Your Weight is {Body_Weight} and your Hight is {Body_Height}, So your BMI is {BMI_Cal}")

