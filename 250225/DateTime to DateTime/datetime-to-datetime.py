a, b, c = map(int, input().split())

# Write your code here!
the_day = a*24*60+b*60+c
day = 11*24*60+11*60+11
print(the_day-day)