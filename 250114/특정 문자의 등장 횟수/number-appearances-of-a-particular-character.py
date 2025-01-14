s = input()
cnt_1 = 0
cnt_2 = 0

for i in range(len(s)-1):
    if s[i:i+2] == "ee":
        cnt_1 += 1
    elif s[i:i+2] == "eb":
        cnt_2 += 1

print(cnt_1, cnt_2)