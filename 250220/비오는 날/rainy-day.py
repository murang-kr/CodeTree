n = int(input())
arr = [tuple(input().split()) for _ in range(n)]

class Information:
    def __init__(self, e1, e2, e3):
        self.date = e1
        self.week = e2
        self.weather = e3

infor = []
for i in range(n):
    infor.append(Information(arr[i][0], arr[i][1], arr[i][3]))

answer = None
for obj in infor:
    if obj.weather == "Rain":
        if answer == None:
            answer = obj
        else:
            y1, m1, d1 = map(int, obj.date.split("-"))
            y2, m2, d2 = map(int, answer.date.split("-"))
            if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 < d2):
                answer = obj

print(answer.date, answer.week, answer.weather)
