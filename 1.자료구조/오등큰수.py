from sys import stdin # 시간 초과 나중에 다시 풀어보기,
# 딕셔너리 구조를 이용하여 시간 줄일 수 있었다.
# 마지막 이중 for 문 구조를 조금 줄일 수 있을 것 같다. 내 코드 속도 2900ms 다른 사람 코드 속도 1900ms

Test_case = int(stdin.readline().strip())
num_array = list(map(int, stdin.readline().strip().split()))
appear_array = dict()
out_array = ['-1' for _ in range(Test_case)]

num_stack = []

for i in num_array:
    try:
        appear_array[i] += 1
    except:
        appear_array[i] = 1

for i in range(Test_case):

    if not len(num_stack):
        num_stack.append(i)

    elif appear_array[num_array[num_stack[-1]]] >= appear_array[num_array[i]]:
        num_stack.append(i)

    elif appear_array[num_array[num_stack[-1]]] < appear_array[num_array[i]]:
        for _ in range(len(num_stack)):
            if appear_array[num_array[num_stack[-1]]] < appear_array[num_array[i]]:
                out_array[num_stack[-1]] = str(num_array[i])
                num_stack.pop()
            else:
                break

    num_stack.append(i)

print(' '.join(out_array))
