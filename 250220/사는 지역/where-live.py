n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Write your code here!
class Information:
    def __init__(self, e1, e2, e3):
        self.name = e1
        self.address = e2
        self.city = e3

infor = []
for i in range(n):
    infor.append(Information(name[i], street_address[i], region[i]))

answer = infor[0]
for obj in infor[1:]:
    if answer.name < obj.name:
        answer = obj

print("name", answer.name)
print("addr", answer.address)
print("city", answer.city)