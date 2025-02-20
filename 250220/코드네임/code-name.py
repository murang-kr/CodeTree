MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Write your code here!
class Agent:
    def __init__(self, e1, e2):
        self.codename = e1
        self.score = e2

agents = []
for i in range(MAX_N):
    agents.append(Agent(codenames[i], scores[i]))

min_val = 100
lower_agent = None
for obj in agents:
    if obj.score < min_val:
        min_val = obj.score
        lower_agent = obj
print(lower_agent.codename, lower_agent.score)