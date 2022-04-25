# BFS 의 경우 스페셜저지를 만족시키려면 1. 시작 정점으로 부터의 거리가 오름차순, 2. 먼저 들어간 자식노드의 자식노드가 차례로 나와야함
# DFS 의 경우 스페셜저지를 만족시키려면 1. 먼저 들어간 자식노드의 자식노드 부터 출력하되 자식 노드 끼리의 순서는 상관 없

# 종료 시점에서 len(node[cur]) 과 부모노드의 호출 count가 같지 않을 때

from sys import stdin

N = int(stdin.readline().strip())
node = [[] for _ in range(N+1)]
check = [False] * (N+1)
check[1] = [0, 1]

for i in range(N-1):
    A, B = map(int, stdin.readline().split())
    node[A].append(B)
    node[B].append(A)

def DFS(cur, stack):

    for child in node[cur]:
        if check[child] == False:
            stack.append(child)
            check[child] = [cur, len(stack)]
            DFS(child, stack)

    if len(stack):
        stack.pop()
        if len(stack):
            cur = stack[-1]
            DFS(cur, stack)
    else:
        return

goal = list(map(int, stdin.readline().split()))
stack = [1]
DFS(1, stack)

parent = 0
size = 1
status = 1

for cur in goal:
    print(parent, size, check[cur][0], check[cur][1], node[cur])
    if len(node[cur]) == 1:
        continue

    elif parent == check[cur][0] and size == check[cur][1]:
        parent = cur
        size += 1

    else:
        status = 0
        break

print(status)