arr = ["L", "E", "B", "R", "O", "S"]
char = input()
flag = True
for i, c in enumerate(arr):
    if c == char:
        print(i)
        flag = False
        break
if flag:
    print("None")