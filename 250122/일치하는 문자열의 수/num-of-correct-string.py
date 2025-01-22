n, A = input().split()
s = [input() for _ in range(int(n))]
cnt = 0
for word in s:
    if word == A:
        cnt += 1
print(cnt)