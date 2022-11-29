# DFS 는 stack 재귀 깊이
# BFS 는 queue 너비

from sys import stdin, stdout

def DFS(index, N, V, check, node, output):
    #if index >= N:
    #    return stdout.write(' '.join(map(str ,output)) + '\n')

    check[V] = True
    for o in node[V]:
        if check[o] == False:
            output.append(o)
            DFS(index+1, N, o, check, node, output)

    if index == 1:
        return stdout.write(' '.join(map(str, output)) + '\n')
    else:
        return

def BFS(N, V, node):
    index = 0
    Que = [V]
    output = []
    check = [False] * (N+1)
    check[V] = True

    while len(Que):
        output.append(V)
        for o in node[V]:
            if check[o]:
                continue
            check[o] = True
            Que.append(o)
        index += 1
        Que.pop(0)
        if len(Que):
            V = Que[0]

    return stdout.write(' '.join(map(str, output)))

N, M, V = map(int,stdin.readline().split())

node = [[] for _ in range(N+1)]
check = [False] * (N+1)
output = []

for i in range(M):
    A, B = map(int, stdin.readline().split())
    node[A].append(B)
    node[B].append(A)

for i in range(1, N+1):
    node[i].sort()
output.append(V)

DFS(1, N, V, check, node, output)
BFS(N, V, node)