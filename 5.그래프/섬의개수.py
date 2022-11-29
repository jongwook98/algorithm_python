from sys import stdin

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break

    island_arr = [[] for _ in range(h)]
    check = [[False] * w for _ in range(h)]
    count = 0

    for i in range(h):
        island_arr[i] = list(map(int, stdin.readline().split()))

    for Y in range(h):
        for X in range(w):
            if check[Y][X] == False:
                if island_arr[Y][X]:
                    count += 1
                    Que_y = [Y]
                    Que_x = [X]
                    check[Y][X] = True
                    # -> 이 아래서부터 BFS 인데, 함수로 구현하지 않으니 코드가 복잡해보인다. 함수로 구현해보는 연습하자.
                    while len(Que_y):
                        cur_y = Que_y[0]
                        cur_x = Que_x[0]
                        for i in range(len(dx)):
                            ny = cur_y + dy[i]
                            nx = cur_x + dx[i]
                            if 0 <= ny < h and 0 <= nx < w:
                                if check[ny][nx] == False:
                                    if island_arr[ny][nx]:
                                        Que_y.append(ny)
                                        Que_x.append(nx)
                                        check[ny][nx] = True
                        Que_x.pop(0)
                        Que_y.pop(0)

    print(count)