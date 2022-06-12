from sys import stdin

N, L = map(int, stdin.readline().split())
Map_arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

count = 0

for y in range(N):
    for x in range(N):
        print(y, x, count)
        if x == 0:
            flag = 0
            last_h = 0
            cur_h = Map_arr[y][x]
            equal_height = 1
        else:
            last_h = cur_h
            cur_h = Map_arr[y][x]

        if equal_height == 0:
            equal_height = 1

        if flag == 1 and equal_height >= L:
            equal_height = 0
            flag = 0

        if last_h != 0 and last_h == cur_h:
            equal_height += 1
            if flag == 1 and equal_height >= L:
                equal_height = 1
                flag = 0

        elif last_h != 0 and abs(last_h - cur_h) >= 2:
            flag = 2
            break
        elif last_h != 0:
            if cur_h - last_h == 1 and equal_height >= L:
                equal_height = 1
            elif cur_h - last_h == 1:
                flag = 2
                break
            elif last_h - cur_h == 1:
                equal_height = 1
                flag += 1
                if flag > 1:
                    break
    if flag == 0:
        count += 1

for x in range(N):
    for y in range(N):
        print(y, x, count)
        if y == 0:
            flag = 0
            last_h = 0
            cur_h = Map_arr[y][x]
            equal_height = 1
        else:
            last_h = cur_h
            cur_h = Map_arr[y][x]

        if equal_height == 0:
            equal_height = 1

        if flag == 1 and equal_height >= L:
            equal_height = 0
            flag = 0

        if last_h != 0 and last_h == cur_h:
            equal_height += 1
            if flag == 1 and equal_height >= L:
                equal_height = 1
                flag = 0

        elif last_h != 0 and abs(last_h - cur_h) >= 2:
            flag = 2
            break
        elif last_h != 0:
            if cur_h - last_h == 1 and equal_height >= L:
                equal_height = 1
            elif cur_h - last_h == 1:
                flag = 2
                break
            elif last_h - cur_h == 1:
                equal_height = 1
                flag += 1
                if flag > 1:
                    break
    if flag == 0:
        count += 1

print(count)