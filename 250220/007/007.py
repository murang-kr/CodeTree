c, p, t = input().split()

class C:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

C1 = C(c, p, t)

print("secret code :", C1.code)
print("meeting point :", C1.place)
print("time :", C1.time)