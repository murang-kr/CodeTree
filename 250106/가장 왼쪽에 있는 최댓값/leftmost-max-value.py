n = int(input())
a = list(map(int, input().split()))

# Write your code here!
max_val = max(a)
idx = a.index(max_val)
while True:
    print(idx+1, end = " ")
    if idx == 0:
        break
    max_val = max(a[:idx])
    idx = a.index(max_val)