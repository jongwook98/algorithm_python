from collections import deque

N = int(input())

CARD = deque()
for i in range(N, 0, -1):
    CARD.append(i)

for i in range(N-1):
    CARD.pop()
    CARD.appendleft(CARD.pop())

print(CARD[0])
