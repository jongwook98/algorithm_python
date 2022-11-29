#BFS 로 1이 있는 지점을 Queue에 넣고 계속 찾는과정 반복 -> check[I] == False 일 때 다시 들어가서 반복
#집의 수를 append 한 다음에 배열의 개수 출력, sort해서 출력하면 될듯

from sys import stdin

N = int(stdin.readline())
space_arr = [[] for _ in range(N)]
check = [[False] * N for _ in range(N)]

partition = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    space_arr[i] = list(map(int, stdin.readline().strip()))

for Y in range(N):
    for X in range(N):
        if space_arr[Y][X]:
            if check[Y][X] == False:
                Que_y = [Y]
                Que_x = [X]
                check[Y][X] = True
                count = 0
                while len(Que_y):
                    cur_y = Que_y[0]
                    cur_x = Que_x[0]
                    count += 1
                    for i in range(4):
                        ny = cur_y + dy[i]
                        nx = cur_x + dx[i]
                        if 0 <= ny < N and 0 <= nx < N:
                            if check[ny][nx] == False:
                                if space_arr[ny][nx]:
                                    Que_y.append(ny)
                                    Que_x.append(nx)
                                    check[ny][nx] = True
                    Que_y.pop(0)
                    Que_x.pop(0)
                partition.append(count)
partition.sort()
print(len(partition))
for i in range(len(partition)):
    print(partition[i])


''' 맞긴 했는데 코드길이가 너무 길다.. 위는 좌표에 따른 상하좌우 반복문을 하나로 줄인 코드
from sys import stdin

N = int(stdin.readline())
space_arr = [[] for _ in range(N)]
check = [[False] * N for _ in range(N)]

partition = []

for i in range(N):
    space_arr[i] = list(map(int, stdin.readline().strip()))

for Y in range(N):
    for X in range(N):
        if space_arr[Y][X]:
            if check[Y][X] == False:
                Que_y = [Y]
                Que_x = [X]
                check[Y][X] = True
                count = 0
                while len(Que_y):
                    cur_y = Que_y[0]
                    cur_x = Que_x[0]
                    count += 1
                    for i in range(4):
                        if i == 0:
                            if cur_y-1 >= 0:
                                if check[cur_y-1][cur_x] == False:
                                    if space_arr[cur_y-1][cur_x]:
                                        Que_y.append(cur_y-1)
                                        Que_x.append(cur_x)
                                        check[cur_y-1][cur_x] = True
                        elif i == 1:
                            if cur_x+1 < N:
                                if check[cur_y][cur_x+1] == False:
                                    if space_arr[cur_y][cur_x+1]:
                                        Que_y.append(cur_y)
                                        Que_x.append(cur_x+1)
                                        check[cur_y][cur_x+1] = True
                        elif i == 2:
                            if cur_y+1 < N:
                                if check[cur_y+1][cur_x] == False:
                                    if space_arr[cur_y+1][cur_x]:
                                        Que_y.append(cur_y+1)
                                        Que_x.append(cur_x)
                                        check[cur_y+1][cur_x] = True
                        else:
                            if cur_x-1 >= 0:
                                if check[cur_y][cur_x-1] == False:
                                    if space_arr[cur_y][cur_x-1]:
                                        Que_y.append(cur_y)
                                        Que_x.append(cur_x-1)
                                        check[cur_y][cur_x-1] = True
                    Que_y.pop(0)
                    Que_x.pop(0)
                partition.append(count)
partition.sort()
print(len(partition))
for i in range(len(partition)):
    print(partition[i])
'''