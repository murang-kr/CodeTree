sex = int(input())
age = int(input())

if sex == 1:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")
else:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")