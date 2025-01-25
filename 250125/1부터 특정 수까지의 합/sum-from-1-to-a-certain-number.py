n = int(input())

# Write your code here!
def custom(num):
    sum_val = 0
    for i in range(1, num+1):
        sum_val += i
    sum_val /= 10
    return int(sum_val)

print(custom(n))