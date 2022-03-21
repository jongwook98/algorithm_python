from sys import stdin
#최대공약수 구하는 알고리즘 - 유클리드 호제법

def find_GCP(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return find_GCP(b, r)

Test_case = int(stdin.readline())

for _ in range(Test_case):
    total_GCP = 0
    num_array = list(map(int, stdin.readline().strip().split()))
    for n in range(1, num_array[0]):
        for m in range(n+1, num_array[0]+1):
            total_GCP += find_GCP(num_array[n], num_array[m])

    print(total_GCP)
