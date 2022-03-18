Test_case = int(input())
stack = []
print_stack = []
in_num = 1
error_flag = 0

for _ in range(Test_case):
    out_num = int(input())

    while in_num <= out_num:
        stack.append(in_num)
        print_stack.append('+')
        in_num = in_num + 1

    while True:
        try:
            pop_num = stack.pop()
            print_stack.append('-')
            if pop_num == out_num:
                break
        except:
            error_flag = 1
            break

if error_flag == 1:
    print("NO")
else:
    for sym in range(len(print_stack)):
        print(print_stack[sym])
