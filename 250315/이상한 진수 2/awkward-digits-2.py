a = list(input())

# Please write your code here.
for i in range(len(a)):
    if a[i] == "0":
        a[i] = "1"
        break

a = "".join(a)
print(int(a, 2))