from collections import deque

mv = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def solution(places):

    answer = []

    for place in places:
        person = []
        check = [[False for _ in range(5)] for _ in range(5)]
        Que = deque()

        flag = True

        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    Que.append([y, x, 0, 5])
                    check[y][x] = True
        while Que:
            cur_y, cur_x, dis, dir_ = Que.popleft()
            if dis >= 2:
                answer.append(1)
                flag = False
                Que.clear()
                break

            for i in range(4):
                ny, nx = cur_y + mv[i][0], cur_x + mv[i][1]
                if 0 <= ny < 5 and 0 <= nx < 5 and (dir_+2) % 4 != i:
                    if check[ny][nx] is False and place[ny][nx] == 'O':
                        Que.append([ny, nx, dis + 1, i])
                        check[ny][nx] = True
                    elif place[ny][nx] == 'P':

#                         for sh in range(5):
#                             print(check[sh])
#                         print()

                        answer.append(0)
                        flag = False
                        Que.clear()
                        break
        if flag:
            answer.append(1)

    return answer