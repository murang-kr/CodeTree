temp = list(map(int, input().split()))
sum_val = sum(temp[1::2])
print(sum_val, f"{sum(temp[2::3])/len(temp[2::3]):.1f}")