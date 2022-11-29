from sys import stdin

# 걸린시간 2056 ms
# 다른사람 코드 164 ms
# 이유는?

# 내 코드는 경계선을 나누고 전체맵을 탐색하여 선거구의 인덱스로 더하는 방법
# 경계선을 나누고 내부 지역까지 5번 선거구로 나누기 위해 해당 행에서 최소 최대 사이값 5로 지정

# 다른 사람 코드는 경계선을 나누지 않고 주어진 수식으로 바로 해당 선거구에 더하는 방법

N = int(stdin.readline().strip())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

min_sub = 1000000

# 전부 브루트포스 되는지 확인하기

def make_brute(N):
    for y in range(N-2):
        for d1 in range(1, N - y - 1):
            for d2 in range(1, N - y - d1 - 1):
                for x in range(N):
                    if y+d1+d2 < N and 0 <= x-d1 and x+d2 < N:
#                       print(y, x, d1, d2)
                        BFS(y, x, d1, d2)

# 선거구 나누기
# 5의 내부를 5로 바꿔주어야 함
def BFS(y, x, d1, d2):
    sep_Map = [[False for _ in range(N)] for _ in range(N)]
    sep_line = [[] for _ in range(N)]

    for dis in range(d1+1):
        sep_line[y + dis].append(x - dis)
        sep_line[y + d2 + dis].append(x + d2 - dis)
        sep_Map[y + dis][x - dis] = 5
        sep_Map[y + d2 + dis][x + d2 - dis] = 5
    for dis in range(d2+1):
        sep_line[y + dis].append(x + dis)
        sep_line[y + d1 + dis].append(x - d1 + dis)
        sep_Map[y + dis][x + dis] = 5
        sep_Map[y + d1 + dis][x - d1 + dis] = 5

    # 5번 선거구
    for i in range(N):
        if len(sep_line[i]):
            if min(sep_line[i]) == max(sep_line[i]):
                continue
            else:
                for j in range(1, max(sep_line[i]) - min(sep_line[i])):
                    sep_Map[i][min(sep_line[i]) + j] = 5


    for abs_y in range(N):
        for abs_x in range(N):
            if sep_Map[abs_y][abs_x] is False:
                if abs_y < y + d1 and abs_x <= x:
                    sep_Map[abs_y][abs_x] = 1
                elif abs_y <= y + d2 and x < abs_x < N:
                    sep_Map[abs_y][abs_x] = 2
                elif y + d1 - 1 <= abs_y < N and abs_x < x - d1 + d2:
                    sep_Map[abs_y][abs_x] = 3
                else:
                    sep_Map[abs_y][abs_x] = 4

#    for i in range(N):
#        print(sep_Map[i])

    calcul_pop(sep_Map)

def calcul_pop(sep_Map):
    global min_sub

    population = [0, 0, 0, 0, 0]
    for y in range(N):
        for x in range(N):
            population[sep_Map[y][x] - 1] += Map[y][x]

#    print(max(population), min(population), max(population) - min(population))
    min_sub = min(min_sub, max(population) - min(population))

if __name__=="__main__":
    make_brute(N)
    print(min_sub)

# x, y , d1, d2 브루트포스로 모든 경우 정하기
# 해당 범위안의 인구수 각 지역별로 더하기
# 차이가 가장 많이 나는 선거구 인구 빼기
# 끝까지 반복 후 가장 적은 인구 수의 차 출력