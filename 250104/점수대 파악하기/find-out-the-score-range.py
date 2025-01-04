cnt_arr = [0 for _ in range(10)]
arr = list(map(int, input().split()))
for item in arr:
    if item == 0:
        break
    if item > 9:
        cnt_arr[(item//10)-1] += 1

cnt_arr.reverse()
for i in range(len(cnt_arr)):
    print(f"{100-(i*10)} - {cnt_arr[i]}")