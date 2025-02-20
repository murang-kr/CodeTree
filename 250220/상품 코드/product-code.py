product_name, product_code = input().split()
product_code = int(product_code)

# Write your code here!
class Information:
    def __init__(self, e1, e2):
        self.name = e1
        self.code = e2

infor1 = Information("codetree", 50)
infor2 = Information(product_name, product_code)
print(f"product {infor1.code} is {infor1.name}")
print(f"product {infor2.code} is {infor2.name}")