 #       ***CODING EXERCISE***

# # 1.Create a Tuple:
# tuple = ("vinay", "24", "blue")
# print(tuple)

# # 2.Access Tuple Elements:
# days_ = ('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
# print(days_[4])

# # 3. Tuple Concatenation:
# odd = (1,3,5,7,9)
# even = (2,4,6,8,10)
# resulth = (odd + even)
# print(resulth)

# # 4.Tuple Unpacking:
# rectangle = (10,20)
# length,width = rectangle
# area = length * width
# print("length:",length)
# print("width:",width)
# print("area of the rectangle:",area)

# # 5.Check if an Element Exists
# names = ('bahubali','saaho','kalki',)
# element = input("enter a element to check: ")
# if element in names :
#     print(f"{element},exits in the tuple.")
# else :
#     print(f"{element},does not exist in tuple.")


# # 6. Write a Python program to generate a bill for a supermarket purchase
# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# print("items  price")
# print("-"*15)
# total_cost = sum(price for _, price in items)
# for item,price in items:
#     print(f"{item}  {price:.2f}")
# print("-"*15)
# print(f"total, {total_cost:.2f}")