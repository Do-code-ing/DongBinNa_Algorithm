# [서로소 집합 자료구조: 경로 압축]

# 찾기(Find) 함수를 최적화하기 위한 방법으로 경로 압축(Path Compression)을 이용할 수 있습니다.
#   - 찾기(Find) 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신합니다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 경로 압축 기법을 적용하면 각 노드에 대하여 찾기(Find) 함수를 호출한 이후에
#   해당 노드의 루트 노드가 바로 부모 노드가 됩니다.
# 동일한 예시에 대해서 모든 합집합(Union) 함수를 처리한 후 각 원소에 대하여
#   찾기(Find) 함수를 수행하면 다음과 같이 부모 테이블이 갱신됩니다.
# 기본적인 방법에 비하여 시간 복잡도가 개선됩니다.
# 노드 번호     1   2   3   4   5
# 부모          1   1   1   1   1


# [서로소 집합 자료구조 구현: 경로 압축]

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