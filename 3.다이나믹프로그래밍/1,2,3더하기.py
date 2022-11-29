# 1, 2, 3 의 합으로 나타내는 방법은
# D[i-1] D[i-2] D[i-3]으로 구할 수 있을 듯

method_of_sum = [0 for _ in range(11)]
method_of_sum[1] = 1
method_of_sum[2] = 2
method_of_sum[3] = 4

Test_case = int(input())
for _ in range(Test_case):
    N = int(input())
    if N >= 4:
        for i in range(4, N+1):
            if not method_of_sum[i]:
                method_of_sum[i] = method_of_sum[i-1] + method_of_sum[i-2] + method_of_sum[i-3]
        print(method_of_sum[N])
    else:
        print(method_of_sum[N])