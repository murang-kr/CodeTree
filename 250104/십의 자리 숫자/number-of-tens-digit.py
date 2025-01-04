cnt_arr = [0 for _ in range(9)]
arr = list(map(int, input().split()))
for item in arr:
    if item == 0:
        break
    if item > 9:
        cnt_arr[(item//10)-1] += 1

for i in range(len(cnt_arr)):
    print(f"{i+1} - {cnt_arr[i]}")