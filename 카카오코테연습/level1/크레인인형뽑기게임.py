from collections import deque

def solution(board, moves):

    Que = deque()
    Que.append(-1)
    answer = 0

    for index in moves:
        for y in range(len(board[0])):
            if board[y][index - 1]:
                if Que[-1] == board[y][index - 1]:
                    Que.pop()
                    answer += 2
                else:
                    Que.append(board[y][index - 1])

                board[y][index - 1] = 0
                break


    return answer

# 불필요한 deque 사용을 금지한다