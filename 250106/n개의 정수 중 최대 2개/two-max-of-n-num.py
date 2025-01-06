n = int(input())
a = list(map(int, input().split()))

# Write your code here!
import sys
first = -sys.maxsize
second = -sys.maxsize

for num in a:
    if num > first:
        first, second = num, first
    elif num > second:
        second = num
print(first, second)