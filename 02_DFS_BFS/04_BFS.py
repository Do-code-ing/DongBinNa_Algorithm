# [BFS] (Breadth-First Search)
# BFS는 너비 우선 탐색이라고 부르며, 그래프에서 가장 가까운 노드부터 우선적으로 탐색하는 알고리즘입니다.
# BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
#   1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
#   2. 큐에 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리합니다.
#   3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.
# 특정 조건에서의 최단 경로 문제를 해결하기 위해 사용될 수 있다.

# BFS 소스코드 예제

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=" ")
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8], # <-1
    [1, 7], # <-2
    [1, 4, 5], # <-3
    [3, 5], # <-4
    [3, 4], # <-5
    [7], # <-6
    [2, 6, 8], # <-7
    [1, 7] # <-8
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9
# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
print()