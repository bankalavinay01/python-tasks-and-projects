#*****CODING EXERCISE*****

# #task-1: Reverse list
# list=[10,20,30,40,50,11]
# list.reverse()
# print(list)

# #task-2: Common Elements
# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]
# list3=[]
# for i in list1:
#     if i in list2:
#      list3.append(i)
# print(list3)

# #task-3: unique elements
# list1=[1,2,2,3,4,4,5]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# #task-4: remove duplicates
# clean_list = []
# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# for i in duplicated_list:
#     if i not in clean_list :
#         clean_list.append(i)
# print(clean_list)

#LIST COMPREHENSIONS

# #1-Square numbers: create a list of square of numbers from 1 to 10.
# list_squares = [i**2  for i in range(1,11)]
# print(list_squares)

# #2-Even Numbers: Generate a list of even numbers from 1 to 20.
# even = [i for i in range(1,21) if i%2==0]
# print(even)

# #3-Words Lengths: Given a list of words, create a list containing the lengths of each word.
# words = ["apple", "banana", "cherry", "date"]

# words_length = [len(word) for word in(words) ]
# print (words_length)








