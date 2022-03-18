Test_case = int(input())

for _ in range(Test_case):
    stack = []
    VPS = input()
    for index in range(len(VPS)):
        if VPS[index] == '(':
            stack.append(index)

        elif VPS[index] == ')':
            try:
                stack.pop()
            except:
                print('NO')
                break
        if index == len(VPS)-1:
            if len(stack):
                print('NO')
            else:
                print('YES')
