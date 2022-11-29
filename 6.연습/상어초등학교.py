from sys import stdin

# 시키는대로 작성했더니 구현
# 좋아하는 친구, 빈자리가 없는 경우를 만족시키기 위해 처음 best_score 값을 -1 로 초기화 해야했음

N = int(stdin.readline())
st_list = [list(map(int, stdin.readline().split())) for _ in range(N ** 2)]

place = [[[False, 0] for _ in range(N)] for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for i in range(N ** 2):
    best_y, best_x, best_score = 0, 0, -1
    for y in range(N):
        for x in range(N):
            if place[y][x][0] is False:
                seat_score = 0
                for n in range(4):
                    ny = y + dy[n]
                    nx = x + dx[n]
                    if 0 <= ny < N and 0 <= nx < N:
                        # 좋아하는 학생
                        if place[ny][nx][0] in st_list[i][1:]:
                            seat_score += 10
                        # 비어있는 칸 개수세기
                        if place[ny][nx][0] is False:
                            seat_score += 1

                        if seat_score > best_score:
                            best_y, best_x, best_score = y, x, seat_score

    place[best_y][best_x][0] = st_list[i][0]
    place[best_y][best_x][1] = i

sum_ = 0

for y in range(N):
    for x in range(N):
        cur_i = place[y][x][1]
        count = -1

        for n in range(4):
            ny = y + dy[n]
            nx = x + dx[n]
            if 0 <= ny < N and 0 <= nx < N:
                if place[ny][nx][0] in st_list[cur_i][1:]:
                    count += 1

        if count == -1:
            continue
        sum_ += 10 ** count

print(sum_)