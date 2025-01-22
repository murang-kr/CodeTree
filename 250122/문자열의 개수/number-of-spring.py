cnt = 0
arr = []
while True:
    s = input()
    if s == "0":
        break
    else:
        cnt += 1
        if cnt % 2 == 1:
            arr.append(s)

print(cnt)
for word in arr:
    print(word)