# [서로소 집합]

# 서로소 집합(Disjoint Sets)란 공통 원소가 없는 두 집합을 의미합니다.
# {1, 2}와 {3, 4}는 서로소 관계이다.
# {1, 2}와 {2, 3}은 서로소 관계가 아니다.


# [서로소 집합 자료구조]

# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조입니다.
# 서로소 집합 자료구조는 두 종류의 연산을 지원합니다.
#   - 합집합(Union): 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산입니다.
#   - 찾기(Find): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산입니다.
# 서로소 집합 자료구조는 합치기 찾기(Union Find) 자료구조라고 불리기도 합니다.

# 여러 개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정은 다음과 같습니다.
#   1. 합집합(Union) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인합니다.
#       1) A와 B의 루트 노드 A', B'를 각각 찾습니다.
#       2) A'를 B'의 부모 노드로 설정합니다.
#   2. 모든 합집합(Union) 연산을 처리할 때까지 1번의 과정을 반복합니다.


# [서로소 집합 자료구조: 동작 과정 살펴보기]

# 처리할 연산들: Union(1, 4), Union(2, 3), Union(2, 4), Union(5, 6)


# [서로소 집합 자료구조: 연결성]

# 기본적인 형태의 서로소 집합 자료구조에서느 루트 노드에 즉시 접근할 수 없습니다.
#   - 루트 노드를 찾기 위해 부모 테이블을 계속해서 확인하며 거슬러 올라가야 합니다.
# 다음 예시에서 노드 3의 루트를 찾기 위해서는 노드 2를 거쳐 노드1 에 접근해야 합니다.
# 노드번호  1   2   3
# 부모      1   1   2


# [서로소 집합 자료구조: 기본적인 구현 방법]

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x): # parent : 부모 테이블, x : 노드 번호
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x: # 노드 번호와 노드 번호에 입력되어 있는 부모 번호가 다르면
        return find_parent(parent, parent[x]) # 입력되어 있는 부모 번호로 재귀 호출 
    return x

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

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end="")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end="")
for i in range(1, v+1):
    print(parent[i], end=" ")


# [서로소 집합 자료구조: 기본적인 구현 방법의 문제점]

# 합집합(Union) 연산이 편향되게 이루어지는 경우 찾기(Find) 함수가 비효율적으로 동작합니다.
# 최악의 경우에는 찾기(Find) 함수가 모든 노드를 다 확인하게 되어 시간 복잡도가 O(V)입니다.
#   - 다음과 같이 {1,2,3,4,5}의 총 5개의 원소가 존재하는 상황을 확인해 봅시다.
#   - 수행된 연산들: Union(4,5), Union(3,4), Union(2,3), Union(1,2)
# 노드 번호     1   2   3   4   5
# 부모          1   1   2   3   4