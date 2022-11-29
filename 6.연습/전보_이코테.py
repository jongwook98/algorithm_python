import heapq
from sys import stdin
from collections import defaultdict


input = stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())

distance = [INF for _ in range(N + 1)]
graph = defaultdict(list)

for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Z, Y))

def dijkstra(start):
    h = []

    distance[start] = 0
    heapq.heappush(h, (0, start))

    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue

        for cost, next_ in graph[now]:
            if distance[next_] > distance[now] + cost:
                heapq.heappush(h, (distance[now] + cost, next_))
                distance[next_] = distance[now] + cost

dijkstra(C)

max_time = 0
cnt = 0

for i in distance:
    if i > 0 and i is not INF:
        cnt += 1
        max_time = max(max_time, i)

print(cnt, max_time)