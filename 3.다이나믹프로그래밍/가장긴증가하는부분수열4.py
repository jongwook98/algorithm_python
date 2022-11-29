''' 백준 코드

다이나믹 프로그래밍의 식을 생각해내는 것이 어렵네,

n = int(input())
a = list(map(int,input().split()))
d = [0]*n
v = [-1]*n
for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[j]+1 > d[i]:
            d[i] = d[j]+1
            v[i] = j
ans = max(d)
p = [i for i,x in enumerate(d) if x == ans][0]
print(ans)
def go(p):
    if p == -1:
        return
    go(v[p])
    print(a[p],end=' ')
go(p)
print()
'''

from sys import stdin

N = int(stdin.readline())

D_length = [0 for _ in range(N+1)]
D_ptr = [-1 for _ in range(N+1)]

arr = list(map(int, stdin.readline().split()))

for n in range(N):
    D_length[n] = 1
    for m in range(n):
        if arr[m] < arr[n] and D_length[m]+1 > D_length[n]:
            D_length[n] = D_length[m]+1
            D_ptr[n] = m

print(max(D_length))

out_arr = []
out_num = D_length.index(max(D_length))

while True:
    out_arr.append(arr[out_num])
    out_num = D_ptr[out_num]
    if out_num == -1:
        break

for i in range(len(out_arr)-1, -1, -1):
    if i != 0:
        print(out_arr[i], end= ' ')
    else:
        print(out_arr[i])