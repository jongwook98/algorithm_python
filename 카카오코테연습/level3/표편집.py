# 시간초과를 넘기지 않기위한 링크드 리스트, 복구시 stack 자료구조 이용

def solution(n, k, cmd):
    linked_list = {}
    stack = []

    def Cut(cur):
        stack.append([cur] + linked_list[cur])
        left, right = linked_list[cur]

        if left is False:
            linked_list[right] = [False, linked_list[right][1]]
            cur = linked_list[cur][1]
        elif right is False:
            linked_list[left] = [linked_list[left][0], False]
            cur = linked_list[cur][0]
        else:
            linked_list[left] = [linked_list[left][0], right]
            linked_list[right] = [left, linked_list[right][1]]
            cur = linked_list[cur][1]

        return cur

    def ctrl_z(cur):
        pos, r_left, r_right = stack.pop()

        if r_left is False:
            linked_list[r_right] = [pos, linked_list[r_right][1]]
        elif r_right is False:
            linked_list[r_left] = [linked_list[r_left][0], pos]
        else:
            linked_list[r_left] = [linked_list[r_left][0], pos]
            linked_list[r_right] = [pos, linked_list[r_right][1]]

        return cur

    for i in range(n):
        if i == 0:
            linked_list[i] = [False, i + 1]
        elif i == n - 1:
            linked_list[i] = [i - 1, False]
        else:
            linked_list[i] = [i - 1, i + 1]

    cur = k
    for comm in cmd:
        order = comm.split()
        if order[0] == 'C':
            cur = Cut(cur)
        elif order[0] == 'Z':
            cur = ctrl_z(cur)
        elif order[0] == 'D':
            for _ in range(int(order[1])):
                cur = linked_list[cur][1]
        else:
            for _ in range(int(order[1])):
                cur = linked_list[cur][0]

    answer = ['O' for _ in range(n)]
    for cur, _, _ in stack:
        answer[cur] = 'X'

    return ''.join(answer)