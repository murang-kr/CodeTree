n = int(input())
a = list(map(int, input().split()))

# Write your code here!
first = a[0]
second = a[0]

for num in a[1:]:
    if num > first:
        first, second = num, first
    elif num > second:
        second = num
print(first, second)