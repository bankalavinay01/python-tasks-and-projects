 #       *** BVK-MARKET ***

name=input("enter your name:")

#list of items
list='''
rice        Rs 25/kg
oil         Rs 5/liter
mirchi      Rs 2/kg
salt        Rs 1/kg
haldi       Rs 500/grams
sugar       Rs 5/kg
milk        Rs 3/packets
colgate     Rs 50/box
soap        Rs 4/pieces
ariel       Rs 5/liters
'''

#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rate for each item
items={'rice': 25, 'oil':5, 'mirchi': 2, 'salt': 1,'haldi':500, 'sugar': 5, 'milk': 3, 'colgate': 50, 'soap': 4, 'ariel': 5,}

while True:
    option=input("press 1 for list or 2 to exit:")
    if option=='2':
        print("thank you for shopping")
        break
    elif option=='1':
        print(list)

        while True:
            inp1=input("to buy press 1 or press 2 to exit:")
            if inp1=='2':
                print("thank you for shopping")
                break
            elif inp1=='1':
                item=input("choose your item:")
                quantity=int(input("enter quantity:"))
            if item in items:
                price=quantity*(items[item])
                pricelist.append((item,quantity,price))
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                tax=(totalprice*5)/100
                finalprice=tax+totalprice
            else:
                print("item is invalid")
        else:
            print("entered number is invalid")
        inp=input("bill the items yes or no:")
        if inp=='yes':
            pass
            if finalprice!=0:
                print("-"*20,"BVK-Supermarket","-"*20)
                print(" "*25,"hyderabad")
                print("Name:",name)
                print("-"*63)
                print("sno"," "*10,"items"," "*11,"quantity"," "*10,"price")
                for i in range(len(pricelist)):
                    print(i," "*13,ilist[i]," "*15,qlist[i]," "*15,plist[i])
                print("-"*63)
                print(" "*35,"total amount:","Rs",totalprice)
                print("tax amount"," "*35,"tax Rs",tax)
                print("-"*63)
                print(" "*35,"finalamount:","Rs",finalprice)
                print("-"*63)
                print(" "*20,"Thank you for shopping! visit again.")
                print("-"*63)
        break