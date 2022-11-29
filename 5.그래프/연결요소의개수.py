from sys import stdin

N, M = map(int, stdin.readline().split())

count = 0

node = [[] for _ in range(N+1)]
check = [False] * (N+1)
for i in range(M):
    u, v = map(int, stdin.readline().split())
    node[u].append(v)
    node[v].append(u)

for i in range(1, N+1):
    if check[i] == False:
        count += 1
        check[i] = True
        Que = [i]
        while len(Que):
            cur = Que[0]
            for o in node[cur]:
                if check[o] == False:
                    Que.append(o)
                    check[o] = True
            Que.pop(0)

print(count)