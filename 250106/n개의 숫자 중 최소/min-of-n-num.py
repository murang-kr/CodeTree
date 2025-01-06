n = int(input())
a = list(map(int, input().split()))

# Write your code here!
min_val = a[0]
for num in a[1:]:
    if num < min_val:
        min_val = num

print(min_val, a.count(min_val))