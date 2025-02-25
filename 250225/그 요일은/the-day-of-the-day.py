m1, d1, m2, d2 = map(int, input().split())
A = input()

# Write your code here!
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
first_day = sum(num_of_days[0:m1])+d1
second_day = sum(num_of_days[0:m2])+d2
difference = second_day - first_day
difference_of_week = week.index(A)
print(((difference-difference_of_week)//7)+1)