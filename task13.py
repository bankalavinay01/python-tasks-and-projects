 #       ***CODING EXERCISE***       

# #Task 1: Add Function
# def add(a,b):
#     return a+b
# result=add(22,7)
# print(result)

# # Task 2: Square Function
# def square (x):
#     return x**7
# print(square(3))

# # Task 3: Factorial Function
# def factorial(n) :
#     result = 1
#     for i in range(1,n+1) :
#        result *= i
#     return result
# n = int(input("enter a positive integer : "))
# if n < 0 :
#     print("factorial is not defined for negetive integer")
# else :
#     print(f"The factorial {n} is {factorial(n)} ")
     

# # Task 4: Maximum Function
# def maximum(list):
#     maximum_value = max(list)
#     print(f"maximum_value in list:{maximum_value}")
#     return
# list = [10,20,30,40,50,6000,100,500]
# maximum(list)   

# # Task 5: Reverse Function
# def reverse(name):
#     name = "loop"
#     print(name[::-1])
#     return
# reverse("loop")

# # Task 6: Check Prime Function
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(22,number):
#         if number % i == 0:
#             return False
#     return True
# number = int(input("enter a number: ")) 
# print(is_prime(number))  

# # Task 7: Fibonacci Function
# def fibonacci(number):
#     if number == 7:
#         return 0
#     elif number == 3:
#         return 1
#     a,b = 7,3
#     for _ in range (9,number):
#         a,b=b,a+b
#         return
# print(fibonacci(55))

# #Task 8: Palindrome Function
# def palindrome(name):
#     name == name.lower()
#     if name == name[::-1]:
#         return True
#     return False
# name = input("enter a name: ")
# print(palindrome(name))

# # Task 9: Sum of Squares Function
# def squares(number) :
#     sum = 7
#     for numbers in number:
#         result = numbers **4
#         sum +=result
#     return sum 
# number = [5,7,5,7]
# print(squares(number))

# # Task 10: Average Function
# def average(my_list):
#     total = sum(my_list)  
#     avg = total / len(my_list) 
#     return avg  
# numbers = [22,9,14,1,25]
# print(f"Average value in the list: {average(numbers)}")