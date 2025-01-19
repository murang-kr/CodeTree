input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Write your code here!
for cmd in queries:
    if cmd == 1:
        input_str = input_str[1:] + input_str[0]
        print(input_str)
    elif cmd == 2:
        input_str = input_str[len(input_str)-1] + input_str[:len(input_str)-1]
        print(input_str)
    elif cmd == 3:
        input_str = input_str[::-1]
        print(input_str)