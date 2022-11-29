from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M
use = [False] * (N+1)

def ascend_arr(count, N, M):
    if count == M:
#        for m in range(M):
        stdout.write(' '.join(map(str,output)) + '\n') # 이 방법으로 포맷팅 하면 사이 형식을 지정할 수 있어서 좋은듯...
#            print(output[m], end= ' ')
#        print()
        return
    for i in range(1, N+1):
        if use[i]:
            continue
        for under in range(i+1):
            use[under] = True
        output[count] = i
        ascend_arr(count+1, N, M)
        for under in range(i+1):
            use[under] = False

ascend_arr(0, N, M)