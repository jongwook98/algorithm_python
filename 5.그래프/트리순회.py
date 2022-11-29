# 전위 순회 - 처음부터 사용하고 있었던 DFS
# 후위 순회 - DFS 요소를 stack에서 빠져나가는 순간에 저장   --- 후위 순회를 자주 사용한다. 트리 알고리즘 대부분 사용 
# 중위 순회 - 루트 노트가 자식 가운데에 있는 순회 방법으로, 왼쪽 자식이 이미 저장되어 있을 때 루트노드 저장, 오른쪽 자식 탐색으로 작성함.

from sys import stdin

N = int(stdin.readline().strip())
node = [[] for _ in range(N+1)]

check = [False] * (N+1)

for i in range(N):
    start, left, right = stdin.readline().split()
    if left == '.':
        left = chr(64)
    if right == '.':
        right = chr(64)

    node[ord(start) - 64] = [ord(left)-64, ord(right)-64]

def fore_DFS(cur, stack):

    check[cur] =True
    for i in node[cur]:
        if check[i] == False:
            stack.append(i)
            output.append(chr(i+64))
            fore_DFS(i, stack)

    if len(stack):
        stack.pop()
        if len(stack):
            cur = stack[-1]
            fore_DFS(cur, stack)

def middle_DFS(cur, stack):

    for i in node[cur]:
        if check[i] == False:
            if i == node[cur][0]:
                stack.append(node[cur][0])
                check[node[cur][0]] = True
                middle_DFS(node[cur][0], stack)

            else:
                output.append(chr(cur+64))
                stack.append(node[cur][1])
                check[node[cur][1]] = True
                middle_DFS(node[cur][1], stack)

    if len(stack):
        stack.pop()
        if (chr(cur+64)) not in output:
            output.append(chr(cur+64))
        if len(stack):
            cur = stack[-1]
            middle_DFS(cur, stack)

def back_DFS(cur, stack):

    check[cur] =True
    for i in node[cur]:
        if check[i] == False:
            stack.append(i)
            back_DFS(i, stack)

    if len(stack):
        stack.pop()
        output.append(chr(cur+64))
        if len(stack):
            cur = stack[-1]
            back_DFS(cur, stack)

stack_list = [1]
check[1] = True
check[0] = True
output = ['A']
fore_DFS(1, stack_list)
print(''.join(output))

check = [False] * (N+1)
stack_list = [1]
check[1] = True
check[0] = True
output = []
middle_DFS(1, stack_list)
print(''.join(output))
check = [False] * (N+1)

stack_list = [1]
check[1] = True
check[0] = True
output = []

back_DFS(1, stack_list)
print(''.join(output))