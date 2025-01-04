n = int(input())
cnt_arr = [0 for _ in range(9)]
arr = list(map(int, input().split()))
for item in arr:
    cnt_arr[item-1] += 1

for item in cnt_arr:
    print(item)