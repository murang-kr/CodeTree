n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Write your code here!
def  is_continuous_partial_sequence(m_seq, s_seq):
    for i in range(len(m_seq)-len(s_seq)+1):
        if m_seq[i] == s_seq[0]:
            if m_seq[i:i+len(s_seq)] == s_seq:
                return True
    return False

if is_continuous_partial_sequence(a, b):
    print("Yes")
else:
    print("No")