#"Who will pay the bill?"
import random

names = input("Enter the everybody's name separated by comma:")
names_list=names.split(",")
print(names_list)

length=len(names_list)
random_choice=random.randint(0,length-1)
print(f"{names_list[random_choice]} will pay the bill")
