n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
arr = []
nums.sort()
for i in range(n):
    arr.append(nums[i] + nums[len(nums)-1-i])

print(max(arr))