from sys import stdin

N, M = map(int, stdin.readline().split())

parent = [i for i in range(N + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    order, a, b = map(int, stdin.readline().split())
    if order == 0:
        union_parent(parent, a, b)
    else:
        if parent[a] == parent[b]:
            print("YES")
        else:
            print("NO")

print(parent)

"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""