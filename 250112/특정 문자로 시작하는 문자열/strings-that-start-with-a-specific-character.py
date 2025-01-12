n = int(input())
arr = [input() for _ in range(n)]
char = input()
sum_len = 0
cnt = 0

for word in arr:
    if word[0] == char:
        sum_len += len(word)
        cnt += 1

print(f"{cnt} {sum_len/cnt:.2f}")