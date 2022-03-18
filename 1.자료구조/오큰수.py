from sys import stdin

Test_case = int(stdin.readline().strip())
num_array = list(map(int, stdin.readline().strip().split()))
out_array = ['-1' for i in range(Test_case)]

num_stack = []

for i in range(Test_case):

    if not len(num_stack):
        num_stack.append(i)

    elif num_array[num_stack[-1]] >= num_array[i]:
        num_stack.append(i)

    elif num_array[num_stack[-1]] < num_array[i]:
        for _ in range(len(num_stack)):
            if num_array[num_stack[-1]] < num_array[i]:
                out_array[num_stack[-1]] = str(num_array[i])
                num_stack.pop()
            else:
                break

    num_stack.append(i)

print(' '.join(out_array))