# 내 코드 -> 38점 시간초과 코드
# 개선점 heapq를 통한 우선순위 큐 구현하기, 산봉우리 확인할 때 list안에 있는지 확인 x set 구조 안에 있는 원소인지 확인하기

# 시작점에서 도착점까지만 가고, 가능 중 걸리는 중간에 거리값의 최대가 작은 것을 출력
from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    answer = defaultdict(int)
    summits = set(summits)
    s = []

    def climb(pos, fin, check, intensity):

        if pos in fin:
            intensity[0] = pos
            if answer[intensity[0]] == 0 or answer[intensity[0]] > intensity[1]:
                answer[intensity[0]] = intensity[1]
            return True

        for n_node in node[pos]:
            if check[n_node[0]] is False:
                check[n_node[0]] = True

                temp = intensity[1]

                if intensity[1] < n_node[1]:
                    intensity[1] = n_node[1]

                climb(n_node[0], fin, check, intensity)
                check[n_node[0]] = False
                intensity[1] = temp

    node = [[] for _ in range(n + 1)]
    for path in paths:
        node[path[0]].append((path[1], path[2]))
        node[path[1]].append((path[0], path[2]))

    for gate in gates:
        check = [False for _ in range(n + 1)]
        check[gate] = True
        climb(gate, summits, check, [0, 0])

    n_list = sorted(answer.items(), key=lambda x: (x[1], x[0]))

    return n_list[0]


# 다른사람 코드

from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    answer = []
    graph = defaultdict(list)
    s = []
    INF = float('inf')
    node_intensity_info = [INF]*(n+1)
    # set 을사용하지않으면 list 내의 in 확인은 O(N) 이라 시간초과뜬다
    summits= set(summits)
    # 출발지점 의 (intensitiy는 0 으로 , gate 번호)
    for g in gates:
        heapq.heappush(s,(0,g))
        node_intensity_info[g] = 0
    # 출발지점 -> 도착지점 -> 출발지점
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
    # 출발지점 돌면서
    while s:
        inten,node = heapq.heappop(s)
        if node in summits or inten > node_intensity_info[node]:
            continue
        # node 의 inten 저장해주고
        for next_node,next_intensity in graph[node]:
            # 현재 intensity 와 다음 노드로가는 next_intensity 와 node_intensity_info 를 비교해야함
            # 즉 intensity 에는 현재와 다음 노드 intensity 를 비교해주고
            intensity = max(inten,next_intensity)
            # 그게 기록일지 (next_node_info) 보다 작다면 갱신해주고 heap 에넣어줌
            if intensity < node_intensity_info[next_node]:
                node_intensity_info[next_node] = intensity
                heapq.heappush(s,(node_intensity_info[next_node],next_node))
    answer = []
    for summit in summits:
        answer.append([summit,node_intensity_info[summit]])
    answer.sort(key = lambda x: (x[1],x[0]))
    return answer[0]