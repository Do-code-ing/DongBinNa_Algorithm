# 어떤 나라에는 N개의 도시가 있다.

# 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
# C에서 보낸 메세지를 받는 도시의 총 개수와 총 걸리는 시간을 출력하라

import sys
from heapq import *
INF = float("INF")

def ikstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

n, m, c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))

ikstra(c)

city = 0
time = 0
for i in distance:
    if i != INF:
        time = max(time, i)
        city += 1
        
print(f"{city-1} {time}")


# [문제 해결 아이디어]

# 핵심 아이디어: 한 도시에서 다른 도시까지의 최단 거리 문제로 치환할 수 있습니다.
# N과 M의 범위가 충분히 크기 때문에 우선순위 큐를 활용한 다익스트라 알고리즘을 구현합니다.
