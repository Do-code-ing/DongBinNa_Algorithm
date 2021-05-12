# 미래도시에는 1번부터 N번까지의 회사가 있다.
# 도로로 연결되어 있다.
# 방문 판매원은 1번 회사에 위치해 있다.
# X번 회사에 방문해 물건을 판매하려고 한다.

# 연결된 두 회사는 양뱡향으로 이동할 수 있다.
# 가중치는 1이다.

# 판매원은 소개팅 참석도 하기 위해 1번 회사에서 출발하여 K번 회사를 방문한 뒤 X번 회사로 가는 것이 목표다.

# 방문 판매원이 이동하는 최소 시간을 계산하시오.

import sys
INF = float("INF")

n, m = map(int, sys.stdin.readline().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

x, k = map(int, sys.stdin.readline().split())

def floyd():
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

floyd()

distance = graph[1][k] + graph[k][x] 
print(distance if distance < INF else -1)


# [문제 해결 아이디어]
# 핵심 아이디어: 전형적인 최단거리 문제이므로 최단거리 알고리즘을 이용해 해결합니다.
# N의 크기가 최대 100이므로 플로이드 워셜 알고리즘을 이용해도 효율적으로 해결할 수 있습니다.
# 플로이드 워셜 알고리즘을 수행한 뒤에 (1번 노드에서 X까지의 최단 거리 + X에서 K까지의 최단 거리)를
# 계산하여 출력하면 정답 판정을 받을 수 있습니다.

