#nested if
# a = 51
#
# if a%2 == 0:
#     print("Even")
#     if(a>30):
#         print("Number is greater than 30..great!")
# print("Bye")

#nested elif

# height = int(input("Enter your height: "))
#
# if height>=3:
#     print("can ride")
#     age = int(input("Enter your age: "))
#     if age<=18:
#         print("please pay 250 Rs")
#     else:
#         print("please pay 500 Rs")
# else:
#     print("Cannot ride")
# print("Bye")

height = int(input("Enter your height: "))

if height>=3:
    print("can ride")
    age = int(input("Enter your age: "))
    if age<=12:
        print("please pay 150 Rs")
    elif age>=18:
        print("please pay 250 Rs")
    else:
        print("Please pay 500 Rs")
else:
    print("Cannot ride")
print("Bye")