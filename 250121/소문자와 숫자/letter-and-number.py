s = input()
answer = ""
for c in s:
    if c.isalpha() or c.isdigit():
        answer += c

print(answer.lower())