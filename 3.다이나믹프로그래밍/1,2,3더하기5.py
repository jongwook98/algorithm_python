# 1,2,3 더하기처럼
# 다이나믹 프로그래밍으로 계산했을 때
# 마지막 수를 나타내는 배열 3개를 각각 저장한다음
# 계산하고 나서 빼주면 어떨까? -> 메모리 초과

# 2차원 배열을 선언해서 마지막으로 끝나는 수를 저장해놓기,

method_sum = [[0]*4 for _ in range(100001)] # 파이썬의 2차원 배열 선언 및 초기화 방법

method_sum[1][1] = 1;
method_sum[2][2] = 1;
method_sum[3][3] = 1; method_sum[3][2] = 1; method_sum[3][1] = 1;

Test_case = int(input())
for i in range(4, 100001):
    method_sum[i][1] = (method_sum[i-1][2] + method_sum[i-1][3]) % 1000000009
    method_sum[i][2] = (method_sum[i-2][1] + method_sum[i-2][3]) % 1000000009
    method_sum[i][3] = (method_sum[i-3][1] + method_sum[i-3][2]) % 1000000009

for _ in range(Test_case): # 입력을 받을 때 위의 반복문을 포함시킨다면 당연히 시간초과가 발생하지..
                           # 배열에 미리 저장해놓은 다음 출력만 하는 방법으로
    N = int(input())
    print(sum(method_sum[N])%1000000009)

'''
#D[i] = D[i-1] - fin_one[i-1] + D[i-2] - fin_two[i-2] + D[i-3] - fin_three[i-3] 결과는 이거지만

#fin_one[i] = D[i-1] - fin_one[i-1] -> D[i-2]
#fin_two[i] = D[i-2] - fin_two[i-2] -> D[i-4]
#fin_three[i] = D[i-3] - fin_three[i-3] -> D[i-6]

#메모리 초과,,
method_sum = [0] * 100001

fin_one = [0] * 100001
fin_two = [0] * 100001
fin_three =[0] * 100001

fin_one[1] = 1
fin_two[2] = 1
fin_one[3] = 1; fin_two[3] = 1; fin_three[3] = 1

method_sum[1] = 1
method_sum[2] = 1
method_sum[3] = 3

Test_case = int(input())
for _ in range(Test_case):
    N = int(input())
    if N >= 4:
        for i in range(4, N+1):
            if method_sum[i] == 0:
                fin_one[i] = method_sum[i-1] - fin_one[i-1]         fin_one[i-1] = method_sum[i-2] - fin_one[i-2]
                fin_two[i] = method_sum[i-2] - fin_two[i-2]         fin_two[i-2] = method_sum[i-4] - fin_two[i-4]
                fin_three[i] = method_sum[i-3] - fin_three[i-3]     fin_three[i-3] = method_sum[i-6] - fin_three[i-6]
                method_sum[i] = method_sum[i-1] + method_sum[i-2] + method_sum[i-3] - fin_one[i-1] - fin_two[i-2] - fin_three[i-3]
                
    print(method_sum[N])
'''