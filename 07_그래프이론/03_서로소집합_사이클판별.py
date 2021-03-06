# [서로소 집합을 활용한 사이클 판별]

# 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있습니다.
#   - 참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있습니다.
# 사이클 판별 알고리즘은 다음과 같습니다.
#   1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인합니다.
#       1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합(Union) 연산을 수행합니다.
#       2) 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것입니다.
#   2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복합니다.


# [서로소 집합을 활용한 사이클 판별: 동작 과정 살펴보기]

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

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")