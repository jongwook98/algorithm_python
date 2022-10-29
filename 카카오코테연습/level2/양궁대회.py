answer = []
max_diff = 0

def cal(info, final):
    A, L = 0, 0
    for i in range(10):
        if info[i] > 0 and info[i] >= final[i]:
            A += (10 - i)
        elif final[i] > 0:
            L += (10 - i)

    return (L - A)


def DFS(n, info, cur_list, index, arrow):
    global max_diff, answer

    if index == 11 or arrow == 0:
        temp = cal(info, cur_list)
        if temp != 0 and temp >= max_diff:
            if temp == max_diff:
                for i in range(10, -1, -1):
                    if answer[i] == cur_list[i]:
                        continue
                    elif answer[i] > cur_list[i]:
                        break
                    else:
                        answer = cur_list[:]
            else:
                max_diff = temp
                cur_list[-1] = arrow

                answer = cur_list[:]

        return True

    if arrow > info[index]:
        cur_list[index] = info[index] + 1
        DFS(n, info, cur_list, index + 1, arrow - cur_list[index])
        cur_list[index] = 0

    DFS(n, info, cur_list, index + 1, arrow)


def solution(n, info):
    DFS(n, info, [0 for _ in range(11)], 0, n)

    if max_diff == 0:
        return [-1]
    else:

        return answer

# 전역 리스트의 경우 전역 리스트 = 리스트 로 복사할 수 없음
# 전역 리스트 = 리스트[:] 와 같이 슬라이싱을 통한 깊은 복사를 해야함..