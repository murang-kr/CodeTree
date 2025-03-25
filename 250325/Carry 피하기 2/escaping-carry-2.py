n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def divider(n):
    ten_thousands = n // 10000
    thousands = (n % 10000) // 1000
    hundreds  = (n % 1000) // 100
    tens      = (n % 100) // 10
    ones      = n % 10

    return [ten_thousands, thousands, hundreds, tens, ones]

max_val = -1
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            fir_vals, sec_vals, thi_vals = divider(arr[i]), divider(arr[j]), divider(arr[k])
            flag = True
            for l in range(5):
                if fir_vals[l] + sec_vals[l] + thi_vals[l] >= 10:
                    flag = False
            if flag:
                max_val = max(max_val, arr[i]+arr[j]+arr[k])

print(max_val)