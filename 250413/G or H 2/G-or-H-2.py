n = int(input())
people = [tuple(input().split()) for _ in range(n)]
people.sort(key = lambda x: int(x[0]))
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
cnt = 0
for i in range(len(people)):
    for j in range(i, len(people)):
        temp = alpha[i:j+1]
        cnt_G, cnt_H = temp.count("G"), temp.count("H")
        if cnt_G == 0 or cnt_H == 0 or cnt_G == cnt_H:
            cnt = max(cnt, int(pos[j]) - int(pos[i]))

print(cnt)