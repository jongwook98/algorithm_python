from collections import deque
import sys

# hash로 나무가 있는 부분만 이동하여 실행하려고 했는데
# 이 같은 경우에 deque list가 나은 이유
# 1. 인덱스로 접근하면 O(1) 복잡도로 접근 가능
# 2. hash의 경우에는 데이터가 많아짐에 따라서 복잡도가 올라가 접근속도가 느려짐
# 3. hash는 접근 속도 목적보다 입력 인덱스가 분산되어 있을 때 list로 모든 공간을 할당하기엔
#    메모리가 커질때 사용한다.

input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
land = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dx, dy = (-1, -1, -1, 0, 0, 1, 1, 1), (-1, 0, 1, -1, 1, -1, 0, 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

def spring_summer():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] <= land[i][j]:
                    land[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, len(trees[i][j])):
                        land[i][j] += trees[i][j].pop() // 2
                    break

def fall_winter():
    for x in range(n):
        for y in range(n):
            for k in range(len(trees[x][y])):
                if trees[x][y][k] % 5 == 0:
                    for d in range(8):
                        nx, ny, = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].appendleft(1)
            land[x][y] += a[x][y]

for _ in range(k):
    spring_summer()
    fall_winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])

print(ans)

'''
from sys import stdin
from collections import defaultdict

# dict으로 구현하였지만 sort해야하는 부분으로 인해 시간초과

N, M, K = map(int, stdin.readline().split()) # N 땅 크기 M 나무 K 몇 년
feed_Map = [list(map(int, stdin.readline().split())) for _ in range(N)]
Map = [[5 for _ in range(N)] for _ in range(N)]

not_sort_tree = defaultdict(list)
tree = defaultdict(list)
dead_tree = defaultdict(list)

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(M):
    x, y, z = map(int, stdin.readline().split())
    not_sort_tree[(y-1, x-1)].append(z)

for loc, olds in not_sort_tree.items():
    y, x = loc
    olds.sort()
    for old in olds:
        tree[(y, x)].append(old)

def spring():
    global tree
    global dead_tree
    new_tree = defaultdict(list)
    new_dead = defaultdict(list)
    for loc, olds in tree.items():
        y, x = loc
        for old in olds:
            if Map[y][x] >= old:
                Map[y][x] -= old
                new_tree[(y, x)].append(old+1)
            else:
                new_dead[(y, x)].append(old)

    tree = new_tree.copy()
    dead_tree = new_dead.copy()

def summer():
    global dead_tree
    for loc, olds in dead_tree.items():
        y, x = loc
        for old in olds:
            Map[y][x] += old // 2

    dead_tree = defaultdict(list)

def fall():
    global tree
    new_tree = defaultdict(list)
    for loc, olds in tree.items():
        y, x = loc
        for old in olds:
            new_tree[(y, x)].append(old)
            if old % 5 == 0:
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < N:
                        new_tree[(ny, nx)].insert(0, 1)
    tree = new_tree.copy()

def winter():
    for y in range(N):
        for x in range(N):
            Map[y][x] += feed_Map[y][x]

if __name__=="__main__":
    for _ in range(K):
        spring()
        summer()
        fall()
        winter()

output = 0
for loc, old in tree.items():
    output += len(old)

print(output)
'''