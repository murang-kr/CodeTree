arr = [input() for _ in range(10)]
char = input()
flag = True

for word in arr:
    if word[-1] == char:
        print(word)
        flag = False

if flag:
    print("None")