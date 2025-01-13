string = input()
answer = ""
for char in string[1::2]:
    answer = "".join([answer, char])

print(answer[::-1])