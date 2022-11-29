# 0 이 가로 1 이 세로
from sys import stdin

max_ = 0
def calcul_(N, M, shape, num_arr):
    global max_
    use_ = [[False] * M for _ in range(N)]
    sum_ = 0
    index = 0

    while index < N*M:
        Y = index // M
        X = index % M
        cur = shape[Y][X]
        num = ''
        index += 1
        if use_[Y][X]:
            continue

        while (Y < N and X < M) and cur == shape[Y][X] and (not use_[Y][X]):
            num += num_arr[Y][X]
            use_[Y][X] = True
            if cur == 1:
                Y += 1
            else:
                X += 1

        sum_ += int(num)

    max_ = max(max_, sum_)
    return

def make_pattern(N, M, index, shape, num_arr):
    if index >= N*M:
        return calcul_(N, M, shape, num_arr)

    Y = index//M; X = index%M
    shape[Y][X] = 0
    make_pattern(N, M, index+1, shape, num_arr)

    shape[Y][X] = 1
    make_pattern(N, M, index+1, shape, num_arr)

N, M = map(int, stdin.readline().split())
num_arr = [0] * N
shape = [[0] * M for _ in range(N)]
for i in range(N):
    num_arr[i] = list(map(str, stdin.readline().strip()))

make_pattern(N, M, 0, shape, num_arr)
print(max_)


''' 갈아엎을것
from sys import stdin

def calcul_(N, M, shape, num_arr):
    use = [0] * (M * N)
    index = 0
    sum_ = 0
    num = ''
    cur = shape[0][0]

    while index < N*M:
        x_index = index // M
        y_index = index % M

        print(index)
        if not use[index]:
            if shape[x_index][y_index] == cur:
                num += num_arr[x_index][y_index]
                use[index] = True
            else:
                sum_ += int(num)
                cur = shape[x_index][y_index]
                num = num_arr[x_index][y_index]
        else:
            if not num == '':
                sum_ += int(num)
                num = ''

        index += 1
    return print(sum_)

def select_shape(N, M, index, shape, num_arr):
    if index == (N*M)-1:
        calcul_(N, M, shape, num_arr)

    x_index = index//M; y_index = index%M

    shape[x_index][y_index] = 0
    select_shape(N, M, index+1, shape, num_arr)

    shape[x_index][y_index] = 1
    select_shape(N, M, index+1, shape, num_arr)

N, M = map(int, stdin.readline().split())
num_arr=[0] * N
shape = [[0] * M for _ in range(N)]

for i in range(N):
    num_arr[i]=list(stdin.readline().strip())

select_shape(N, M, 0, shape, num_arr)
'''