from sys import stdin, stdout

# 이전 순열, 다음 순열을 구하는데 조건문을 잘 생각 해야할 듯

def prev_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] >= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j: #j >= (i-1):
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

while True:
    LOTTO = list(map(int, stdin.readline().split()))

    if not LOTTO[0]:
        break
    select_arr = [1] * 6 + [0] * (LOTTO[0] - 6)

    while True:
        output_arr = []
        for i in range(len(LOTTO)-1):
            if select_arr[i]:
                output_arr.append(LOTTO[i+1])
        stdout.write(' '.join(map(str, output_arr)) + '\n')
        if not prev_permutation(select_arr):
            print()
            break

    # LOTTO[0] 이 입력받은 숫자의 수