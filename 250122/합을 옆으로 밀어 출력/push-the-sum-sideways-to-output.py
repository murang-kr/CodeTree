n = int(input())
arr = [int(input()) for _ in range(n)]

sum_val = str(sum(arr))
sum_val = sum_val[1:]+sum_val[0]
print(sum_val)