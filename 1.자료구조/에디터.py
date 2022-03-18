from sys import stdin

String = list(stdin.readline().strip())
Test_case = int(stdin.readline().strip())

Left_stack = String
Right_stack = []

for _ in range(Test_case):
    order = (stdin.readline().strip()).split()

    if order[0] == 'L':
        if len(Left_stack):
            Right_stack.append(Left_stack.pop())

    elif order[0] == 'D':
        if len(Right_stack):
            Left_stack.append(Right_stack.pop())

    elif order[0] == 'B':
        if len(Left_stack):
            Left_stack.pop()

    elif order[0] == 'P':
        Left_stack.append(order[1])

for w in range(1, len(Right_stack) + 1):
    Left_stack.append(Right_stack[-w])

print(''.join(Left_stack))