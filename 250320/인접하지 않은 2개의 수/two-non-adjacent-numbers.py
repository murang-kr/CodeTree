n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
sum_val = 0
for i in range(n):
    for j in range(n):
        if abs(i-j) >= 2:
            sum_val = max(sum_val, numbers[i]+numbers[j])

print(sum_val)