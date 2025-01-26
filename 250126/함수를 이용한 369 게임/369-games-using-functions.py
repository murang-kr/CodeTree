a, b = map(int, input().split())

# Write your code here!
def three_multiple(n):
    return n % 3 == 0

def have_369(n):
    return "3" in str(n) or "6" in str(n) or "9" in str(n)

cnt = 0
for i in range(a, b+1):
    if three_multiple(i) or have_369(i):
        
        cnt += 1

print(cnt)