from sys import stdin
from collections import deque

N = int(stdin.readline())
K = int(stdin.readline())
Apple_arr = [list(map(int, stdin.readline().split())) for _ in range(K)]

L = int(stdin.readline())
Snake_move = [list(stdin.readline().split()) for _ in range(L)]

Snake_arr = deque()
Snake_arr.appendleft([1, 1])

Snake_Head = [1, 1, 0]

ny = [0, 1, 0, -1]
nx = [1, 0, -1, 0]

count = 0
move_s = 0

while True:
    if move_s < len(Snake_move):
        if count == int(Snake_move[move_s][0]):
            if Snake_move[move_s][1] == 'D':
                Snake_Head[2] = (Snake_Head[2] + 1) % 4
            elif Snake_move[move_s][1] == 'L':
                Snake_Head[2] = (Snake_Head[2] + 3) % 4
            move_s += 1

    Snake_Head[0], Snake_Head[1] = Snake_Head[0] + ny[Snake_Head[2]], Snake_Head[1] + nx[Snake_Head[2]]
    count += 1

    if [Snake_Head[0], Snake_Head[1]] in Snake_arr or not (0 < Snake_Head[0] <= N and 0 < Snake_Head[1] <= N):
        break

    Snake_arr.appendleft([Snake_Head[0], Snake_Head[1]])
    tail = Snake_arr.pop()

    if [Snake_Head[0], Snake_Head[1]] in Apple_arr:
        Snake_arr.append(tail)
        Apple_arr.remove([Snake_Head[0], Snake_Head[1]])

print(count)