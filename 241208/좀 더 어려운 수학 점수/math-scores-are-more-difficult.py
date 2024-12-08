A_math, A_english = map(int, input().split())
B_math, B_english = map(int, input().split())

if A_math > B_math:
    print("A")
elif A_math < B_math:
    print("B")
else:
    if A_english > B_english:
        print("A")
    elif A_english < B_english:
        print("B")