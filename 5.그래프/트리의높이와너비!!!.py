# 이것은 중위 탐색으로 계산하면 편할 듯
# 헤드 루트에 대한 정보가 없음..
from sys import stdin

N = int(stdin.readline().strip())
node = [[] for _ in range(N+1)]
check = [False] * (N+1)
level = [[] for _ in range(N+1)]

head_node = False

output = []
stack_list = [1]

height = 0
max_ = 0

for i in range(N):
    P, A, B = map(int, stdin.readline().split())
    if head_node == False:
        head_node = P
    node[P] = [A, B]

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

check[head_node] = 1

middle_DFS(head_node, stack_list, 2)
print(output, check)
print(level)

for i in range(2, height):
    min_num = min(output[level[i]])
    max_num = max(output[level[i]])
    max_ = max(max_, (max_num - min_num + 1))

print(max_)