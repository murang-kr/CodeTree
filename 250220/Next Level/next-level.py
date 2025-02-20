user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Write your code here!
class C:
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

C1 = C("codetree", 10)
C2 = C(user2_id, user2_level)

print(f"user {C1.e1} lv {C1.e2}")
print(f"user {C2.e1} lv {C2.e2}")