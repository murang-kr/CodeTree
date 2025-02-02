n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
def divide_even(input_list):
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            input_list[i] //= 2
            

divide_even(arr)
for elem in arr:
    print(elem, end = " ")