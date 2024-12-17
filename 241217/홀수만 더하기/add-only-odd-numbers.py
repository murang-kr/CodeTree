sum_val = 0
n = int(input())
for i in range(n):
    temp = int(input())
    if temp % 2 == 1 and temp % 3 == 0:
        sum_val += temp
print(sum_val)