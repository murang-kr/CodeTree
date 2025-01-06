n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
import sys
max_val = -sys.maxsize
for num in nums:
    if num > max_val and nums.count(num) == 1:
        max_val = num

if max_val != -sys.maxsize:
    print(max_val)
else:
    print(-1)