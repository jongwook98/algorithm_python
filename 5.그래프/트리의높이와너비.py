# 맞았는데... 내 코드 실행시간 2000ms 다른 사람 실행시간 100ms
# 헤드 노드를 찾는 과정 -> BFS여서 오래걸렸나, 각 레벨에서 max, min값을 추출하는 과정에서 N만큼 시간을 쓰니, 오래걸렸나

# 이것은 중위 탐색으로 계산하면 편할 듯
# 헤드 루트에 대한 정보가 없음..
import sys
from collections import deque
sys.setrecursionlimit(10**6) # RecursionError 해결방법 재귀함수의 최대 수를 지정하는 것\

N = int(sys.stdin.readline().strip())
node = [[] for _ in range(N+1)]
check = [False] * (N+1)
check[0] = True

head_check = [False] * (N+1)
head_check[0] = True

level = [[] for _ in range(N+1)]

head_node = False

output = []
height = 0
max_ = [0, 0]

Que = deque()

for i in range(N):
    P, A, B = map(int, sys.stdin.readline().split())
    node[P] = [A, B]

def find_head(start_node):
    Que.append(start_node)
    head_check[start_node] = True
    #자식 노드 -1 일 때!!
    while len(Que):
        cur = Que.popleft()
        for i in node[cur]:
            if head_check[i] == False and i != -1:
                head_check[i] = True
                Que.append(i)

    if False not in head_check:
        return start_node
    else:
        return find_head(head_check.index(False))

def middle_DFS(cur, stack, cnt):
    global height
    height = max(cnt, height)
    for i in node[cur]:
        if check[i] == False and i != -1:
            if i == node[cur][0]:
                stack.append(i)
                check[i] = cnt
                level[cnt].append(i)
                middle_DFS(i, stack, cnt+1)

            else:
                output.append(cur)
                stack.append(i)
                check[i] = cnt
                level[cnt].append(i)
                middle_DFS(i, stack, cnt+1)

    if len(stack):
        stack.pop()
        cnt = check[cur] - 1
        if cur not in output:
            output.append(cur)
        if len(stack):
            cur = stack[-1]
            middle_DFS(cur, stack, cnt+1)

head_node = find_head(1)
check[head_node] = 1
level[1] = [head_node]
stack_list = [head_node]
middle_DFS(head_node, stack_list, 2)

for i in range(1, height):
    min_num = 10001
    max_num = 0
    for j in level[i]:
        min_num = min(min_num, output.index(j))
        max_num = max(max_num, output.index(j))

    if max_[1] != max(max_[1], (max_num - min_num + 1)):
        max_[1] = max(max_[1], (max_num - min_num + 1))
        max_[0] = i

print(' '.join(map(str, max_)))
