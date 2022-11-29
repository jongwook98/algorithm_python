prime_arr = [True for _ in range(1000001)]
prime_arr[0] = False
prime_arr[1] = False

output = []

for i in range(2, 1001):
    for t in range(i*2, 1000001, i):
        prime_arr[t] = False

Test_case = int(input())

def matching_prime(N):
    result = 0
    for i in range(2, N//2 + 1):
        if prime_arr[i]:
            if prime_arr[N-i]:
                result += 1

    return result

for _ in range(Test_case):
    candi_num = int(input())
    print(matching_prime(candi_num))