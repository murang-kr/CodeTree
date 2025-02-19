n, k, t = input().split()
n, k = int(n), int(k)
string = [input() for _ in range(n)]

# Write your code here!
arr = []
for word in string:
    if word[:len(t)] == t:
        arr.append(word)

arr.sort()
print(arr[k-1])