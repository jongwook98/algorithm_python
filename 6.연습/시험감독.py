from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B, C = map(int, stdin.readline().split())

sum_director = 0

for j in range(N):
    A[j] -= B
    sum_director += 1

for i in range(N):
    if A[i] > 0:
        if A[i] % C == 0:
            sum_director += A[i] // C
        else:
            sum_director += A[i] // C + 1

print(sum_director)