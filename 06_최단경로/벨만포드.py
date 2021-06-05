# [음수 간선이 포함된 상황에서의 최단 거리 문제]

# 음수 간선에 관하여 최단 경로 문제는 다음과 같이 분류할 수 있습니다.
#   1. 모든 간선이 양수인 경우
#   2. 음수 간선이 있는 경우
#       1. 음수 간선 순환은 없는 경우
#       2. 음수 간선 순환이 있는 경우
# 벨만 포드 최단 경로 알고리즘은 음의 간선이 포함된 상황에서도 사용할 수 있습니다.
#   - 또한 음수 간선의 순환을 감지할 수 있습니다.
#   - 벨만 포드의 기본 시간 복잡도는 O(VE)로 다익스트라 알고리즘에 비해 느립니다.


# 벨만포드 알고리즘은 다음과 같습니다.

#   1. 출발 노드를 설정합니다.
#   2. 최단 거리 테이블을 초기화합니다.
#   3. 다음의 과정을 N-1번 반복합니다.
#       1. 전체 간선 E개를 하나씩 확인합니다.
#       2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신합니다.
# 만약 음수의 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한 번 더 수행합니다.
#   - 이때 최단 거리 테이블이 갱신된다면 음수 간선의 순환이 존재하는 것입니다.


# [벨만포드 VS 다익스트라]

# 다익스트라 알고리즘
#   - 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택합니다.
#   - 음수 간선이 없다면 최적의 해를 찾을 수 있습니다.
# 벨만포드
#   - 매번 모든 간선을 전부 확인합니다.
#       - 따라서 다익스트라 알고리즘에서의 최적의 해를 항상 포함합니다.
#   - 다익스트라 알고리즘에 비해서 시간이 오래 걸리지만 음수 간선 순환을 탐지할 수 있습니다.

import sys
input = sys.stdin.readline
INF = float("inf")

def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    # 전체 n번의 라운드(round)를 반복
    for i in range(n):
        # 매 반복마다 '모든 간선'을 확인하며
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True

    return False

n, m = map(int, input().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])