from sys import stdin

N = int(stdin.readline())
time_ = list(map(int, stdin.readline().split()))
time_.sort()

sum_ = 0
for i in range(N):
    sum_ += (N-i)*time_[i]

print(sum_)