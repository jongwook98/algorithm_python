from sys import stdin

ABCDE = 0

def find_ABCDE(count, me, friend_graph, check):
    global ABCDE
    if count >= 4:
        ABCDE = 1
        return True

    for i in friend_graph[me]:
        if check[i] or ABCDE:
            continue
        check[i] = True
        find_ABCDE(count+1, i, friend_graph, check)
        check[i] = False

N, M = map(int, stdin.readline().split())
friendship = [[] for _ in range(N)]
check = [False] * N
ABCDE = 0

for i in range(M):
    A, B = map(int, stdin.readline().split())
    friendship[A].append(B)
    friendship[B].append(A)

for i in range(N):
    if len(friendship[i]):
        check[i] = True
        find_ABCDE(0, i, friendship, check)
        check[i] = False

print(ABCDE)