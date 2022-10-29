'''
-> 시간초과가 났고,, deque를 쓸거라면 deque와 DFS 조합이 아니라
조건에 따른 pop, append로 가능함

1번 큐의 크기가 더 크면 1번을 pop 해서 2번에 추가
2번 큐의 크기가 더 크면 2번을 pop 해서 1번에 추가
단 종료 시점을 잘 생각해서.!
중복해서 검사하는 일은 없도록

from collections import deque

min_result = -1


def DFS(queue1, queue2, index, over):
    global min_result
    if sum(queue1) == sum(queue2):
        if min_result == -1:
            min_result = index
        min_result = min(min_result, index)
        return

    if index >= over:
        return

    if len(queue1):
        queue2.append(queue1.popleft())
        DFS(queue1, queue2, index + 1, over)

        queue1.appendleft(queue2.pop())

    if len(queue2):
        queue1.append(queue2.popleft())
        DFS(queue1, queue2, index + 1, over)

        queue2.appendleft(queue1.pop())


def solution(queue1, queue2):
    global min_result
    Que1, Que2 = deque(queue1), deque(queue2)
    base = len(Que1) + len(Que2)
    des, res = (sum(Que1) + sum(Que2)) // 2, (sum(Que1) + sum(Que2)) % 2

    if res == 1:
        return -1

    DFS(Que1, Que2, 0, base)
    return min_result
'''

# 이 문제는 부분합 같게 하는 문제였음,, 큐를 이용한 백트래킹은 함정,,,
# 순서가 정해져 있는 배열에서 부분합이 어느정도 인지 나타내는 가장 빠른 알고리즘 -> 투포인터

def solution(queue1, queue2):
    totallist = queue1 + queue2
    total_sum = sum(totallist)

    des, res = total_sum // 2, total_sum % 2
    cur_sum = sum(queue1)
    cnt = 0

    if res == 1:
        return -1

    sp, ep = 0, len(queue1)

    while sp < len(totallist) and ep < len(totallist):
        if cur_sum == des:
            return cnt

        elif cur_sum > des:
            cur_sum -= totallist[sp]
            sp += 1


        else:
            cur_sum += totallist[ep]
            ep += 1

        cnt += 1

    return -1