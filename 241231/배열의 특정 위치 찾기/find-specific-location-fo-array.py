temp = list(map(int, input().split()))
sum_val = sum(temp[1::2])
print(sum_val, f"{sum_val/len(temp[1::2])}")