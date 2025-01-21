A = input()
answer = 0
for c in A:
    if c.isdigit():
        answer += int(c)

print(answer)