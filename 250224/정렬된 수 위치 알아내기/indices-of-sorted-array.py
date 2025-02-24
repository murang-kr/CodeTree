n = int(input())
sequence = list(map(int, input().split()))

# Write your code here!
for i in range(n):
    sequence[i] = [i+1, sequence[i]]

sequence.sort(key=lambda x: x[1])
for i in range(n):
    sequence[i][1] = i+1
sequence.sort(key=lambda x: x[0])
for elem in sequence:
    print(elem[1], end = " ")