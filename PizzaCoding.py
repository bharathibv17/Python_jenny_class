
size = (input("Enter the pizza (small,medium,large): "))
bill = 0

if size == "S" or size == "s":
    bill +=100
    print("Small Pizza Price is 100 Rs.")
elif size == "M" or size == "m":
    bill +=200
    print("Medium Pizza Price is 200 Rs.")
else:
    bill += 300
    print("Large Pizza Price is 300 Rs. ")

add_pepperoni = input("Do you want to add pepperoni(Y/N): ")
if add_pepperoni == "Y" or add_pepperoni =='y':
    if size == "S" or size == "s":
        bill += 30
    else:
        bill +=50
extra_cheese = input("Do you want to add extra cheese(Y/N) ")
if extra_cheese == "Y" or extra_cheese =="y":
    bill += 30
else:
    bill += 50

print(f"Your total bill is {bill}, Thank you!!")
