temp = list(map(int, input().split()))
odd, even = 0, 0
for i in range(len(temp)):
    if i % 2 == 0:
        odd += temp[i]
    else:
        even += temp[i]
if odd > even:
    print(odd-even)
else:
    print(even-odd)