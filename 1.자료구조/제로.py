from sys import stdin

K = int(stdin.readline())

stack = []

for i in range(K):
    Num = int(stdin.readline())
    if Num == 0:
        stack.pop()

    else:
        stack.append(Num)

print(sum(stack))