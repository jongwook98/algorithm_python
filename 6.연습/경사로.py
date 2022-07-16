from sys import stdin

N, L = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]
total_num = 0

# 예전에 못 풀던 문제 해결
# flag와 count의 순서 배치로 인한 문제 였음..
# 단순 구현,,

## 가로 라인 탐색
for y in range(N):
    flag = 0
    base_ = Map[y][0]
    count = 1
    for x in range(1, N):
        if -1 <= base_ - Map[y][x] <= 1:
            if base_ == Map[y][x]:
                count += 1
            elif Map[y][x] - base_ == 1:
                if count >= L:
                    base_ = Map[y][x]
                    count = 1
                else:
                    flag = 2
                    break
            else:
                if flag == 1:
                    break
                count = 1
                flag = 1
                base_ = Map[y][x]
        else:
            flag = 2
            break
        if flag == 1 and count >= L:
            flag = 0
            count = 0
    if flag == 0:
        total_num += 1

for x in range(N):
    flag = 0
    base_ = Map[0][x]
    count = 1
    for y in range(1, N):
        if -1 <= base_ - Map[y][x] <= 1:
            if base_ == Map[y][x]:
                count += 1
            elif Map[y][x] - base_ == 1:
                if count >= L:
                    base_ = Map[y][x]
                    count = 1
                else:
                    flag = 2
                    break
            else:
                if flag == 1:
                    break
                count = 1
                flag = 1
                base_ = Map[y][x]
        else:
            flag = 2
            break
        if flag == 1 and count >= L:
            flag = 0
            count = 0
    if flag == 0:
        total_num += 1

print(total_num)