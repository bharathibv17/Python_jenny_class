height = int(input("Enter your height: "))
bill =0

if height>=3:
    print("can ride")
    age = int(input("Enter your age: "))
    if age<=12:
        bill = 150
        print("Ticket Price is 150 Rs")
    elif age>=18:
        bill = 250
        print("Ticket Price is 250 Rs")
    else:
        bill = 500
        print("Ticket Price is 500 Rs")

    want_photo = input("Do you want to take photo(Y/N)?")
    if want_photo == 'Y' or want_photo == y:
        bill = bill + 50
    elif want_photo == 'N' or want_photo == 'n':
        print(f"Your total bill is {bill}")

else:
    print("Cannot ride")
print("Bye")