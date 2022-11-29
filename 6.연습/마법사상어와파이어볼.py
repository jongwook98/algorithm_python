from collections import defaultdict

# python dictionary 자료구조 활용
#
# key, values로 이루어져있으며
# 반복문으로 사용할 때 key, values 두 값을 가져오려면 dict.items()로 가져오고
#                   key         값만 가져오려면    dict 만 사용
#                   values      값만 가져오려면    dict.values() 사용

# 같은 key에서 값이 여러개인지, 아닌지 확인하기도 쉽다

N, M, K = map(int, input().split())
fireballs = defaultdict(list)

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs[(r-1, c-1)].append((m, s, d))

dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)

def move_fire():
    global fireballs
    new_fireballs = defaultdict(list)
    for loc, info in fireballs.items():

        sy, sx = loc
        for m, s, d in info:
            ny = (sy + dy[d] * s) % N
            nx = (sx + dx[d] * s) % N
            new_fireballs[(ny, nx)].append((m, s, d))

    fireballs = new_fireballs.copy()

def odd_or_even(dirs):
    odd_flag, even_flag = False, False
    for d in dirs:
        if d % 2 == 1:
            odd_flag = True
        if d % 2 == 0:
            even_flag = True

    if odd_flag and even_flag:
        return False
    return True

def fusion_fireballs():
    global fireballs
    new_fireballs = defaultdict(list)

    for loc, info in fireballs.items():
        if len(info) == 1:
            new_fireballs[loc].append(info[0])
            continue

        sum_m, sum_s, dirs = 0, 0, []
        for m, s, d in info:
            sum_m += m
            sum_s += s
            dirs.append(d)
        new_m = int(sum_m / 5)
        if new_m == 0:
            continue
        new_s = int(sum_s/len(info))
        new_dirs = [0, 2, 4, 6] if odd_or_even(dirs) else [1, 3, 5, 7]
        for new_d in new_dirs:
            new_fireballs[loc].append((new_m, new_s, new_d))

    fireballs = new_fireballs.copy()

for _ in range(K):
    move_fire()
    fusion_fireballs()

result = 0
for loc, info in fireballs.items():
    for m, s, d in info:
        result += m

print(result)