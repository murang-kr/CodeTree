s = input()
answer = ""
for c in s:
    if c.isalpha():
        answer += c

print(answer.upper())