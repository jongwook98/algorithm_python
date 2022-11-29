# 중요도를 나타내는 Queue 와 프린터 대기를 나타내는 Queue를 따로 만들면 편할 듯?

from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    Que = deque()
    import_Que = deque()

    N, M = map(int, stdin.readline().split())
    important = list(map(int, stdin.readline().split()))

    for i in important:
        Que.append(i)
    for i in sorted(important, reverse=True):
        import_Que.append(i)

    while len(Que):
        cur = Que.popleft()
        cur_import = import_Que.popleft()

        if cur == cur_import:
            if M == 0:
                print(N - len(Que))
                break
            else:
                if M == 0:
                    M = len(Que) - 1
                else:
                    M = M - 1
                continue

        else:
            Que.append(cur)
            import_Que.appendleft(cur_import)
            if M == 0:
                M = len(Que) - 1
            else:
                M = M - 1
