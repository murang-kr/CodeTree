m1, d1, m2, d2 = map(int, input().split())

# Write your code here!
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
first_day = sum(num_of_days[0:m1])+d1
second_day = sum(num_of_days[0:m2])+d2
difference = second_day - first_day
difference %= 7
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(week[difference])