# https://www.acmicpc.net/problem/11437

import sys
sys.setrecursionlimit(int(1e5))

n = int(input())
parent = [0] * (n+1)
d = [0] * (n+1) # 깊이 기록
c = [0] * (n+1) # 탐색 여부
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue

        parent[y] = x
        dfs(y, depth+1)

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a
    
dfs(1, 0)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))


# https://www.acmicpc.net/problem/11438

import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
LOG = 21 # 2^20 = 1_000_000

n = int(input())
parent = [[0] * LOG for _ in range(n+1)]
d = [0] * (n+1) # 깊이 기록
c = [0] * (n+1) # 탐색 여부
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue

        parent[y][0] = x # 제일 첫 부모만 갱신
        dfs(y, depth+1)

def set_parent():
    dfs(1, 0)
    for j in range(1, LOG):
        for i in range(1, n+1):
            parent[i][j] = parent[parent[i][j-1]][j-1]

def lca(a, b):
    # b가 더 깊도록 조정
    if d[a] > d[b]:
        a, b = b, a
    
    # 깊이가 동일하도록 조정
    for i in range(LOG-1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    
    if a == b:
        return a
    
    # 부모가 같아지도록 조정
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]
    
set_parent()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))