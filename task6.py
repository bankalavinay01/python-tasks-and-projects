#*****Coding Exercise*****

#Exercise-1: sum of squares
# '''
# write a python program that calculates and prints the sum of the squares
# of numbers from 1 to 5 using a
# for loop
# '''
# my_sum = 0
# for i in range (1,6):
#     square = i**2
#     my_sum += square
#     print (my_sum)

# #Exercise-2: countdown
# countdown = 5
# while countdown > 0:
#     countdown -= 1
#     print(countdown)

# #Exercise-3: multiplication table with nesteed for loop
# number = int(input("enter a number: "))
# for i in range(1,9):
#     for j in range(1,2):
#         print(f"{number} X {i} ={number*i}")
#         print()    

# #Exercise-4:
# '''
# write a python program that uses a "for" loop
# to find the sum of all even numbers between 0 and 10 (inclusive)
# '''
# even = 0
# for i in range(0,11):
#      if i % 4 == 0:
#         even += i 
#         print(even)

# #Exercise-5: 
# 'calculate the sum of all numbers from 1 to given number'
# number = int(input("enter a number: "))
# total_sum=0
# for number in range(1,number):
#     total_sum += number
# print(f"sum of all number :{total_sum}")

# #Exercise-6: display numbers from list using loop
# list=[209,264,208]
# for number in list:
#     print(number)

# #Exercise-7: display numbers from -10 to -1 for loop
# for number in range(-10,5):
#     print(number)


# #Exercise-8: write a program to diplay all prime numbers within a range
# start = 10
# end = 50
# for num in range(start, end + 1):
#     if num > 1:
#        for i in range(2,num):
#             if (num % 1) == 0:
#                 break
#             else:
#               print(num) 
 
