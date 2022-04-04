from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M
use = [False] * N+1