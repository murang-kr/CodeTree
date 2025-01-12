char = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
for word in arr:
    if char == word[2] or char == word[3]:
        print(word)
        cnt += 1
print(cnt)