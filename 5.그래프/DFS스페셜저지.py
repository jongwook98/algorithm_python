# BFS 의 경우 스페셜저지를 만족시키려면 1. 시작 정점으로 부터의 거리가 오름차순, 2. 먼저 들어간 자식노드의 자식노드가 차례로 나와야함
# DFS 의 경우 스페셜저지를 만족시키려면 1. 먼저 들어간 자식노드의 자식노드 부터 출력하되 자식 노드 끼리의 순서는 상관 없
# 종료 시점에서 len(node[cur]) 과 부모노드의 호출 count가 같지 않을 때

# 알고리즘 방법을 생각하지 못함
from sys import stdin

N = int(stdin.readline().strip())
node = [[] for _ in range(N+1)]
check = [False] * (N+1)
output = [1]
rank = [-1 for _ in range(N+1)]

for i in range(N-1):
    A, B = map(int, stdin.readline().split())
    node[A].append(B)
    node[B].append(A)

goal = list(map(int, stdin.readline().split()))
# goal 의 자리 인덱스는 무게값이라고 생각하면 됨

for i in range(1, N+1):
    rank[goal[i-1]] = i

for i in range(1, N+1):
    node[i] = sorted(node[i], key=lambda x : rank[x])

# -> 입력으로 주어진 DFS 방문순서로 맞춰줌
# 이 방문 순서로 만들어진 DFS가 같은지 확인

def DFS(index, cur, output):
    if len(output) >= N:
        return output

    check[cur] = True
    for i in node[cur]:
        if check[i] == False:
            output.append(i)
            DFS(index+1, i, output)

DFS(0, 1, output)

if output == goal:
    print(1)
else:
    print(0)

'''
틀림,,
다른 블로그나 백준코드는 입력으로 주어진 DFS 방문 순서로 다시 sort한 후 DFS 알고리즘을 돌렸을 때 맞는지 틀린지를 확인했으며
아래 코드는 방문 순서로 돌렸을 때 예외가 있는지 없는지 파악하는 방법으로 작성하였지만
DFS 스페셜저지에서 생기는 다른 에러를 못찾은것 같다.

import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline().strip())
node = [[] for _ in range(N+1)]

for i in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    node[A].append(B)
    node[B].append(A)

goal = list(map(int, sys.stdin.readline().split()))

status = 1
stack_list = []

visited = [False] * (N+1)
candidate = [1]

for cur in goal:
    stack_list.append(cur)
    if len(candidate) == 0:
        while cur not in node[stack_list[-1]]:
            stack_list.pop()

            if len(stack_list) == 0:
                status = 0
                break
        if len(stack_list) == 0:
            status = 0
            break

        for i in node[stack_list[-1]]:
            if visited[i] == False:
                candidate.append(i)

    if cur in candidate:
        visited[cur] = True
        candidate = []

        for i in node[cur]:
            if visited[i] == False:
                candidate.append(i)


    else:
        status = 0

print(status)
'''