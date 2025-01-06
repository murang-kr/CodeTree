n = int(input())
price = list(map(int, input().split()))

# Write your code here!
profit = 0
for i in range(len(price[:-1])):
    for p in price[i+1:]:
        if price[i] < p and p - price[i] > profit:
            profit = p - price[i]

print(profit)