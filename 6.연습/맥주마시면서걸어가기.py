from sys import stdin
from collections import deque

def BFS():
    N = int(stdin.readline().strip())
    check = [False for _ in range(N)]

    home = list(map(int, stdin.readline().split()))
    con_store = [list(map(int, stdin.readline().split())) for _ in range(N)]
    festival = list(map(int, stdin.readline().split()))

    Que = deque([home])
    while len(Que):
        cur_y, cur_x = Que.popleft()
        if abs(cur_y - festival[0]) + abs(cur_x - festival[1]) <= 1000:
            return print("happy")

        else:
            for num in range(len(con_store)):
                if check[num] is True:
                    continue
                elif abs(cur_y - con_store[num][0]) + abs(cur_x - con_store[num][1]) <= 1000:
                    check[num] = True
                    Que.append((con_store[num][0], con_store[num][1]))

    return print("sad")

if __name__=="__main__":
    T = int(stdin.readline().strip())

    for _ in range(T):
        BFS()