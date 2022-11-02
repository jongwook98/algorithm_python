# 정확성 53.8/53.8 효율성 13.8 코드
# skill을 맞은 영역을 2차원 누적합 배열로 생성해야함

from collections import defaultdict


def solution(board, skill):
    Map = {}
    skill_Map = defaultdict(int)

    for row, colunms in enumerate(board):
        for column, value in enumerate(colunms):
            Map[(row, column)] = value

    for s_type, r1, c1, r2, c2, degree in skill:
        if s_type == 1:
            deg = -degree
        else:
            deg = degree

        skill_Map[(r1, c1, r2, c2)] += deg

    for info, deg in skill_Map.items():
        r1, c1, r2, c2 = info
        for y in range(r1, r2 + 1):
            for x in range(c1, c2 + 1):
                Map[(y, x)] += deg

    new_list = sorted(Map.values(), key=lambda x: x)
    sp, lp = 0, len(new_list) - 1

    while sp < lp:
        mid = (sp + lp) // 2
        if new_list[mid] > 0:
            lp = mid
        else:
            sp = mid + 1

    answer = len(new_list[sp:])

    return answer

# 해설 보고 다시 푼 코드 100/100 + 누적합

from collections import defaultdict

def solution(board, skill):

    Map = {}
    skill_Map = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for row, colunms in enumerate(board):
        for column, value in enumerate(colunms):
            Map[(row, column)] = value

    for s_type, r1, c1, r2, c2, degree in skill:
        if s_type == 1:
            deg = -degree
        else:
            deg = degree

        skill_Map[r1][c1] += deg
        skill_Map[r2 + 1][c2 + 1] += deg
        skill_Map[r1][c2 + 1] -= deg
        skill_Map[r2 + 1][c1] -= deg

    for x in range(len(board[0])):
        for y in range(len(board)):
            skill_Map[y + 1][x] += skill_Map[y][x]

    for y in range(len(board)):
        for x in range(len(board[0])):
            skill_Map[y][x + 1] += skill_Map[y][x]

    for x in range(len(board[0])):
        for y in range(len(board)):
            Map[(y, x)] += skill_Map[y][x]

    new_list = sorted(Map.values(), key = lambda x:x)
    sp, lp = 0, len(new_list) - 1

    while sp < lp:
        mid = (sp + lp) // 2
        if new_list[mid] > 0:
            lp = mid
        else:
            sp = mid + 1

    answer = len(new_list[sp:])

    return answer