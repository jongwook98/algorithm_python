from sys import stdin
from collections import deque
import copy

# 파이썬 리스트를 깊은 복사를 통해 값을 변경했는데 왜 원본 데이터도 변할까??
# copy 모듈의 deepcopy()를 이용했더니 깊은 복사가 되었다.

# 내가 사용했던 방법은 list_dup = list_original[:] 처럼 슬라이싱으로 복사했는데
# 리스트가 오브젝트를 포함할 경우 그 오브젝트들은 얕은복사만 된다고 한다.
# 처리속도는 리스트 슬라이싱이 가장 빠르고 copy 모듈의 deepcopy() 메소드가 가장 느리다.

# 백트래킹하는 코드를 따로 작성하지 않아서 실행속도는 엄청 느리다 : 6500ms 다른 사람들 속도 600ms 10배 정도

N, M = map(int, stdin.readline().split())
LAB_MAP = [[] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_count = 0
virus_init = []

for i in range(N):
    LAB_MAP[i] = list(map(int, stdin.readline().split()))

for y in range(N):
    for x in range(M):
        if LAB_MAP[y][x] == 2:
            virus_init.append((y, x))

# 여기서 부터 브루트 포스 (벽 세우고 아래 시작)
for one in range(N*M-2):
    one_x = one % M
    one_y = one // M
    if LAB_MAP[one_y][one_x] != 0:
        continue

    for two in range(one + 1, N*M-1):
        two_x = two % M
        two_y = two // M
        if LAB_MAP[two_y][two_x] != 0:
            continue

        for three in range(two + 1, N*M):
            three_x = three % M
            three_y = three // M
            if LAB_MAP[three_y][three_x] != 0:
                continue

            lab_map_dup = copy.deepcopy(LAB_MAP)

            lab_map_dup[three_y][three_x] = 1
            lab_map_dup[two_y][two_x] = 1
            lab_map_dup[one_y][one_x] = 1

            count = 0
            Que = deque(virus_init)
            check = [[False for _ in range(M)] for _ in range(N)]

            while len(Que):
                cur_y, cur_x = Que.popleft()
                for i in range(4):
                    nx = cur_x + dx[i]
                    ny = cur_y + dy[i]
                    if 0 <= nx < M and 0 <= ny < N:
                        if lab_map_dup[ny][nx] == 0 and check[ny][nx] == False:
                            Que.append((ny, nx))
                            lab_map_dup[ny][nx] = 2
                            check[ny][nx] = True

            for y in range(N):
                for x in range(M):
                    if lab_map_dup[y][x] == 0:
                        count = count + 1

            max_count = max(max_count, count)

print(max_count)