#        *** CODING-EXERCISE ***
# #task-1:
# '''
# Write a Python function 
# square_all(numbers) that takes a list of numbers as 
# input and returns a new list containing the square of each number in the 
# input list. Use the 
# map() function with a lambda function to implement this.
# '''
# square_all=map(int,input("enter your numbers:").split())
# obj=map(lambda number:number**2,square_all)
# print(list(obj))

# #task-2:
# '''
# Write a Python function 
# filter_positive(numbers) that takes a list of numbers 
# as input and returns a new list containing only the positive numbers from 
# the input list. use the filter() function with a lambda function to implement this'
# '''
# obj = filter(lambda i : i >= 0 , [-9,-8,-7,1,4,3,-6])
# print(list(obj))

# #task-3:
# '''
# Write a Python function 
# calculate_factorial(n) that calculates the factorial of 
# a given number n. Use the 
# reduce() function with an appropriate lambda 
# function to implement this.
# '''
# from functools import reduce
# def calculate_factorial(n):
#     if n==0 or n==1:
#         return 1
#     return reduce(lambda a, b: a * b, range(1, n + 1), 1)
# obj = factorial_of_5 = calculate_factorial(4)
# print(calculate_factorial(4))

# #task-4:
# '''
# Write a Python function 
# count_vowels(string) that takes a string as input and 
# returns the count of vowels (a, e, i, o, u) in the input string. Use the 
# function with an appropriate lambda function to implement this.
# '''
# from functools import reduce
# def count_vowels(string):
#     return reduce(lambda count, char:count + (char in"aeiouAEIOU"),string,0)
# obj = vowels = count_vowels
# print(count_vowels("are you okay ?") )