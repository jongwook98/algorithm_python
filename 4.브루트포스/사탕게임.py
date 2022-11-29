# 바꾸는 방향은 아래, 오른쪽만 고려하면 다 한 번씩 해보는 것일 것 같다.
# 알고리즘은 구현하였으나 candy_board 의 값이 replace 되면 같이 변경됨..
# 주소값이 다른것을 확인했는데도 replace_board 를 스왑하면 candy_board 도 같이 스왑된다..


from sys import stdin

max_candy = 1
N = int(stdin.readline())
candy_board = [["N"] * N for _ in range(N)]
for i in range(N):
    candy_line = stdin.readline().strip()
    for n in range(len(candy_line)):
        candy_board[i][n] = candy_line[n]

def vertical_max_candy(board):
    max_candy_ver = 1
    for x in range(len(board[0])):
        candy_num_ver = 1
        for y in range(len(board[0])-1):
            stand_candy_ver = board[y][x]
            if stand_candy_ver == board[y+1][x]:
                candy_num_ver += 1
                max_candy_ver = max(max_candy_ver, candy_num_ver)

            else:
                max_candy_ver = max(max_candy_ver, candy_num_ver)
                candy_num_ver = 1

    #print("vertical: ", max_candy_ver)

    return max_candy_ver

def horizon_max_candy(board):
    max_candy_hor = 1
    for y in range(len(board[0])):
        candy_num_hor = 1
        for x in range(len(board[0])-1):
            stand_candy_hor = board[y][x]
            if stand_candy_hor == board[y][x+1]:
                candy_num_hor += 1
                max_candy_hor = max(max_candy_hor, candy_num_hor)
            else:
                max_candy_hor = max(max_candy_hor, candy_num_hor)
                candy_num_hor = 1

    #print("horizon: ", max_candy_hor)

    return max_candy_hor


for y in range(N):
    for x in range(N):
        select_candy = candy_board[y][x]
        if x != N-1:
            # replace_board 의 스왑이 제대로 되지 않음
            if select_candy != candy_board[y][x + 1]:
                temp = candy_board[y][x]
                candy_board[y][x] = candy_board[y][x + 1]
                candy_board[y][x + 1] = temp
                max_candy = max(max_candy, horizon_max_candy(candy_board), vertical_max_candy(candy_board))
                temp = candy_board[y][x]
                candy_board[y][x] = candy_board[y][x + 1]
                candy_board[y][x + 1] = temp
        if y != N-1:
            if select_candy != candy_board[y + 1][x]:
                temp = candy_board[y][x]
                candy_board[y][x] = candy_board[y + 1][x]
                candy_board[y + 1][x] = temp
                max_candy = max(max_candy, horizon_max_candy(candy_board), vertical_max_candy(candy_board))
                temp = candy_board[y][x]
                candy_board[y][x] = candy_board[y + 1][x]
                candy_board[y + 1][x] = temp

print(max_candy)
