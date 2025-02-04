text = input()
pattern = input()

# Write your code here!
def custom():
    for i in range(len(text)-len(pattern)+1):
        if text[i] == pattern[0]:
            if text[i:i+len(pattern)] == pattern:
                return i

    return -1

print(custom())