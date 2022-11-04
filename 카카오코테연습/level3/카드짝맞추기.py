from collections import defaultdict, deque
from itertools import permutations

mv = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def solution(board, r, c):
    INF = int(1e9)
    answer = INF

    def find_path(cur_r, cur_c, des_r, des_c, cur_board):
        check_dist = [[False for _ in range(4)] for _ in range(4)]
        Que = deque()
        Que.append((cur_r, cur_c))
        check_dist[cur_r][cur_c] = 1

        while Que:
            cr, cc = Que.popleft()
            for i in range(4):
                nr, nc = cr + mv[i][0], cc + mv[i][1]
                for j in range(1, 4):
                    nnr, nnc = cr + mv[i][0] * j, cc + mv[i][1] * j
                    if 0 <= nnr < 4 and 0 <= nnc < 4:
                        if cur_board[nnr][nnc] != 0:
                            break
                    else:
                        nnr, nnc = nnr - mv[i][0], nnc - mv[i][1]

                if 0 <= nr < 4 and 0 <= nc < 4:
                    if check_dist[nr][nc] is False:
                        Que.append((nr, nc))
                        check_dist[nr][nc] = check_dist[cr][cc] + 1

                if 0 <= nnr < 4 and 0 <= nnc < 4:
                    if check_dist[nnr][nnc] is False:
                        Que.append((nnr, nnc))
                        check_dist[nnr][nnc] = check_dist[cr][cc] + 1

            if check_dist[des_r][des_c] is not False:
                return check_dist[des_r][des_c], des_r, des_c

    def DFS(order, cur_r, cur_c, cur_board, index, check, cnt):

        nonlocal answer

        if index > len(order) - 1:
            answer = min(cnt, answer)
            return

        for num in range(2):
            des_r, des_c = card_dict[order[index]][num]
            if check[index * 2 + num] == 1:
                continue

            check[index * 2 + num] = 1
            mv_cnt, nex_r, nex_c = find_path(cur_r, cur_c, des_r, des_c, cur_board)

            if sum(check[index * 2:index * 2 + 2]) == 2:

                for des_r, des_c in card_dict[order[index]]:
                    cur_board[des_r][des_c] = 0
                DFS(order, nex_r, nex_c, cur_board, index + 1, check, cnt + mv_cnt)

                for des_r, des_c in card_dict[order[index]]:
                    cur_board[des_r][des_c] = order[index]

            else:
                DFS(order, nex_r, nex_c, cur_board, index, check, cnt + mv_cnt)

            check[index * 2 + num] = 0

    card_dict = defaultdict(list)
    card = set()

    order_list = []

    for y in range(4):
        for x in range(4):
            if board[y][x] != 0:
                card_dict[board[y][x]].append((y, x))
                card.add(board[y][x])

    Done_ = [0 for _ in range(len(card) * 2)]
    order_list.extend(permutations(card, len(card)))

    for proc in order_list:
        DFS(proc, r, c, board[::], 0, Done_, 0)

    return answer