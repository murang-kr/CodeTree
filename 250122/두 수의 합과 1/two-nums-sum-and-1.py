a, b = map(int, input().split())
sum_val = str(a+b)
cnt = 0
for c in sum_val:
    if c == "1":
        cnt += 1
print(cnt)