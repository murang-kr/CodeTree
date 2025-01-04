a, b = map(int, input().split())
cnt_arr = [0]*10
while a > 1:
    cnt_arr[a%b] += 1
    a = a//b
sum_val = 0
for item in cnt_arr:
    sum_val += item ** 2
print(sum_val)