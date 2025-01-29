a, o, c = input().split()
a = int(a)
c = int(c)

# Write your code here!

def addition(a, b):
    return a+b
def subtraction(a, b):
    return a-b
def multiplication(a, b):
    return a*b
def division(a, b):
    return int(a/b)

if o == "+":
    print(a, o, c, "=", end = " ")
    print(addition(a, c))

elif o == "-":
    print(a, o, c, "=", end = " ")
    print(subtraction(a, c))

elif o == "*":
    print(a, o, c, "=", end = " ")
    print(multiplication(a, c))

elif o == "/":
    print(a, o, c, "=", end = " ")
    print(division(a, c))

else:
    print("False")