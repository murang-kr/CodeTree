n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
def custom(tup):
    global arr
    print(sum(arr[tup[0]-1:tup[1]]))

for item in queries:
    custom(item)