from sys import stdin

Test_case = int(stdin.readline())

for _ in range(Test_case):
    status = "YES"
    V, E = map(int, stdin.readline().split())
    check = [False] * (V+1)
    node = [[] for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, stdin.readline().split())
        node[a].append(b)
        node[b].append(a)

    for i in range(1, V+1):
        if check[i] == False:
            Que = [i]
            check[i] = 1
            while len(Que):
                cur = Que[0]
                for o in node[cur]:
                    if check[o] == False:
                        Que.append(o)
                        check[o] = 3 - check[cur]
                    else:
                        if check[o] != 3 - check[cur]:
                            status = "NO"
                Que.pop(0)

    print(status)