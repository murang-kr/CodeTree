arr = list(input().split())
sum_val = 0
for word in arr:
    sum_val += len(word)
print(sum_val)