n = int(input())
temp = list(map(float, input().split()))
average = sum(temp) / len(temp)
print(f"{average:.1f}")
if average >= 4.0:
    print("Perfect")
elif average >= 3.0:
    print("Good")
else:
    print("Poor")