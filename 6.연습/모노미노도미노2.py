from sys import stdin
from collections import deque

# deque 에서 중간값을 삭제하고 싶을때는 del deque[index]


N = int(stdin.readline().strip())
score = 0
area = 0

blue_de = [deque() for _ in range(4)]
green_de = [deque() for _ in range(4)]


def gen(t, x, y):
    global blue_de, green_de
    if t == 1:
        blue_de[x].append(1)
        green_de[y].append(1)

    elif t == 2:
        in_gr = max(len(green_de[y]), len(green_de[y + 1]))
        p_gr = min(len(green_de[y]), len(green_de[y + 1]))

        index = y
        if len(green_de[y]) > len(green_de[y + 1]):
            index = y + 1

        for _ in range(p_gr, in_gr):
            green_de[index].append(0)

        green_de[y + 1].append(1)
        green_de[y].append(1)
        blue_de[x].append(1)
        blue_de[x].append(1)

    elif t == 3:
        in_bu = max(len(blue_de[x]), len(blue_de[x + 1]))
        p_bu = min(len(blue_de[x]), len(blue_de[x + 1]))

        index = x
        if len(blue_de[x]) > len(blue_de[x + 1]):
            index = x + 1

        for _ in range(p_bu, in_bu):
            blue_de[index].append(0)

        blue_de[x + 1].append(1)
        blue_de[x].append(1)
        green_de[y].append(1)
        green_de[y].append(1)

    spe()


def spe():
    global score, blue_de, green_de
    rm_bu, sl_bu = [], False
    rm_gr, sl_gr = [], False

    min_bu = 4
    min_gr = 4
    index = 0

    for i in range(4):
        min_bu = min(min_bu, len(blue_de[i]))
        min_gr = min(min_gr, len(green_de[i]))

    if min_bu != 0:
        for j in range(min_bu - 1, -1, -1):
            flag = True
            for i in range(4):
                if blue_de[i][j] == 0:
                    flag = False
                    break
                index = j

            if flag is True:
                rm_bu.append(index)

    if min_gr != 0:
        for j in range(min_gr - 1, -1, -1):
            flag = True
            for i in range(4):
                if green_de[i][j] == 0:
                    flag = False
                    break
                index = j

            if flag is True:
                rm_gr.append(index)

    if len(rm_bu) != 0:
        for rm_index in rm_bu:
            for i in range(4):
                del blue_de[i][rm_index]
            score += 1

    if len(rm_gr) != 0:
        for rm_index in rm_gr:
            for i in range(4):
                del green_de[i][rm_index]
            score += 1

    for i in range(4):
        for j in range(len(blue_de[i]) - 1, -1, -1):
            if blue_de[i][j] == 1:
                break
            else:
                del blue_de[i][j]

    for i in range(4):
        for j in range(len(green_de[i]) - 1, -1, -1):
            if green_de[i][j] == 1:
                break
            else:
                del green_de[i][j]

    for i in range(4):
        if len(blue_de[i]) > 4:
            sl_bu = len(blue_de[i]) - 4

        if len(green_de[i]) > 4:
            sl_gr = len(green_de[i]) - 4

    if sl_bu is not False:
        for i in range(4):
            for _ in range(sl_bu):
                if len(blue_de[i]) != 0:
                    blue_de[i].popleft()

    if sl_gr is not False:
        for i in range(4):
            for _ in range(sl_gr):
                if len(green_de[i]) != 0:
                    green_de[i].popleft()


def count():
    global area
    for y in range(4):
        for x in range(len(blue_de[y])):
            if blue_de[y][x] == 1:
                area += 1

        for x in range(len(green_de[y])):
            if green_de[y][x] == 1:
                area += 1

    return area


for _ in range(N):
    ty, xi, yi = map(int, stdin.readline().split())
    gen(ty, xi, yi)
    # print("blue")
    # for i in range(4):
    #     print(blue_de[i])
    # print()
    # print("green")
    # for i in range(4):
    #     print(green_de[i])

count()
print(score)
print(area)
