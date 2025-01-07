arr = [list(input().split()) for _ in range(5)]
for item in arr:
    for alpha in item:
        print(alpha.upper(), end = " ")
    print()