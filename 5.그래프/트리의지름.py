from sys import stdin
from collections import deque

V = int(stdin.readline().strip())
node = [[] for _ in range(V+1)]
check = [False] * (V+1)

for _ in range(V):
    info = list(map(int, stdin.readline().split()))
    for i in range(1, len(info)-1, 2):
        node[info[0]].append([info[i], info[i+1]])

def BFS(start_node):
    Que = deque()
    Que.append(start_node)
    check[start_node] = 1

    long_dis = 0

    while len(Que):
        cur = Que.popleft()
        for i in range(len(node[cur])):
            if check[node[cur][i][0]] == False:
                check[node[cur][i][0]] = check[cur] + node[cur][i][1]
                Que.append(node[cur][i][0])

    return [max(check), check.index(max(check))]

new_start_node = BFS(1)[1]
check = [False] * (V+1)
print(BFS(new_start_node)[0] - 1)