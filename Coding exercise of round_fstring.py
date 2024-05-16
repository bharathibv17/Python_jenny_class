#write a program for how manys days, weeks, months left until you live for 90 years

current_age = int(input("Enter your age : "))

year_left = 90 - current_age
days_left = year_left * 365
months_left = year_left * 12
weeks_left = year_left * 52

print(f"Hi your current age is {current_age}, you have {year_left} years,{days_left} days,{months_left} months and {weeks_left}weeks")