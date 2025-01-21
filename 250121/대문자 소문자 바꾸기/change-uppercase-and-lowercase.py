s = input()
answer = ""
for c in s:
    if c >= "A" and c <= "Z":
        answer += c.lower()
    else:
        answer += c.upper()

print(answer)