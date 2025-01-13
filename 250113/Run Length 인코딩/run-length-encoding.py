A = input()

# Write your code here!
encoded = [[A[0], 1]]

for char in A[1:]:
    if encoded[-1][0] == char:
        encoded[-1][1] += 1
    else:
        encoded.append([char, 1])
    
cnt = 0
answer = ""
for row in encoded:
    for elem in row:
        cnt += len(str(elem))
        answer = "".join([answer, str(elem)])

print(cnt)
print(answer)