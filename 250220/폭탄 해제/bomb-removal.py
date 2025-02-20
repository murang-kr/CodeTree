code, color, second = input().split()

class Information:
    def __init__(self, e1, e2, e3):
        self.code = e1
        self.color = e2
        self.second = e3

infor = Information(code, color, second)
print("code :", infor.code)
print("color :", infor.color)
print("second :", infor.second)