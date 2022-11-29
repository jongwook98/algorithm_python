from sys import stdin
from collections import deque

A, B = map(int, stdin.readline().split())

Que = deque()
Que.append([A, 1])

def find():
    while len(Que):
        cur, point = Que.popleft()
        if cur == B:
            return print(point)
        if cur * 2 <= B:
            Que.append([cur * 2, point + 1])
        if cur * 10 + 1 <= B:
            Que.append([cur * 10 + 1, point + 1])
    return print(-1)

if __name__ == "__main__":
    find()