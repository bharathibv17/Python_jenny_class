girl_name = (input("Enter the girl name: "))
girl_name.lower()
boy_name = (input("Enter the boy name: "))
boy_name.lower()

name = str(girl_name) + str(boy_name)
t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
true = t + r + u + e

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
love = l + o + v + e

love_score = int(str(true) +str(love))

if love_score < 10 or love_score >90:
    print(f"Your love score is {love_score} and you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is{love_score} and you are alright together")
else:
    print(f"Your love score is {love_score}")

