n = int(input())

# Write your code here!
def custom(num):
    temp = str(num)
    n1, n2 = int(temp[0]), int(temp[1])
    return num % 2 == 0 and (n1 + n2) % 5 == 0

if custom(n):
    print("Yes")
else:
    print("No")