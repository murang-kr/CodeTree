cnt_arr = [0 for _ in range(6)]
arr = list(map(int, input().split()))
for item in arr:
    cnt_arr[item-1] += 1

for i in range(len(cnt_arr)):
    print(f"{i+1} - {cnt_arr[i]}")