n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
sum_val = 0
for i in range(n):
    without_i = numbers[:i-1]+numbers[i+2:]
    for j in without_i:
        sum_val = max(numbers[i]+j, sum_val)

print(sum_val)