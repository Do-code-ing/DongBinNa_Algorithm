# [신장 트리]

# 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미합니다.
#   - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 합니다.


# [최소 신장 트리]

# 최소한의 비용으로 구성되는 신장 트리를 찾아야 할 때 어떻게 해야 할까요?
# 예를 들어 N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아
#   전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우를 생각해 봅시다.
#   - 두 도시 A, B를 선택했을 때 A에서 B로 이동하는 경로가 반드시 존재하도록 도로를 설치합니다.


# [크루스칼 알고리즘]

# 대표적인 최소 신장 트리 알고리즘입니다.
# 그리디 알고리즘으로 분류됩니다.
# 구체적인 동작 과정은 다음과 같습니다.
#   1. 간선 데이터를 비용에 따라 오름차순으로 정렬합니다.
#   2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인합니다.
#       1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킵니다.
#       2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않습니다.
#   3. 모든 간선에 대하여 2번의 과정을 반복합니다.


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x): # parent : 부모 테이블, x : 노드 번호
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x: # 노드 번호와 노드 번호에 입력되어 있는 부모 번호가 다르면
        parent[x] = find_parent(parent, parent[x]) # 입력되어 있는 부모 번호로 재귀 호출 
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b): # 두 노드 번호에 대해서
    a = find_parent(parent, a) # 부모(루트) 노드를 찾고
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a # 갱신
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# [크루스칼 알고리즘 성능 분석]
# 크루스칼 알고리즘은 간선의 개수가 E개일 때, O(ElogE)의 시간 복잡도를 가집니다.
# 크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 간선의 정렬을 수행하는 부분입니다.
#   - 표준 라이브러리를 이용해 E개의 데이터를 정렬하기 위한 시간 복잡도는 O(ElogE)입니다.