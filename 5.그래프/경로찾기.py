from sys import stdin
from collections import deque

N = int(stdin.readline())
graph_arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

node = [[] for _ in range(N)]

for y in range(N):
    for x in range(N):
        if graph_arr[y][x] == 1:
            node[y].append(x)

for i in range(N):
    check = [False for _ in range(N)]
    Que = deque(node[i])

    while len(Que):
        cur = Que.popleft()
        graph_arr[i][cur] = 1
        if check[cur] is False:
            for NODE in range(len(node[cur])):
                Que.append(node[cur][NODE])
            check[cur] = True

for i in range(N):
    for j in range(N):
        print(graph_arr[i][j], end = ' ')
    print()