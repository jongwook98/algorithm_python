from sys import stdin
from collections import deque

# 예전부터 반례로 자꾸 실수하는데
# 출발점과 목적지가 같을 때 자꾸 에러처리 실수를 하는 것 같다.

F, S, G, U, D = map(int, stdin.readline().split())
mv = [U, -D]

def BFS():

    check = [False for _ in range(F + 1)]
    Que = deque([S])
    check[S] = 0

    if S == G:
        return print(0)

    while len(Que):
        cur = Que.popleft()
        for i in range(2):
            des = cur + mv[i]
            if 1 <= des <= F:
                if check[des] is False:
                    check[des] = check[cur] + 1
                    if des == G:
                        return print(check[des])
                    Que.append(des)
    return print("use the stairs")

if __name__=="__main__":
    BFS()