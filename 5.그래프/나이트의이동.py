from sys import stdin
from collections import deque

Test_case = int(stdin.readline().strip())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(Test_case):
    chess_size = int(stdin.readline().strip())
    Que = deque()
    check = [[False] * chess_size for _ in range(chess_size)]

    Y, X = map(int, stdin.readline().split())
    Que.append((Y, X))
    check[Y][X] = 0

    des_y, des_x = map(int, stdin.readline().split())

    while Que:
        cur_y, cur_x = Que.popleft()
        if des_y == cur_y and des_x == cur_x:
            break
        for i in range(len(dx)):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < chess_size and 0 <= nx < chess_size:
                if check[ny][nx] == False:
                    Que.append((ny, nx))
                    check[ny][nx] = check[cur_y][cur_x] + 1

    print(check[cur_y][cur_x])