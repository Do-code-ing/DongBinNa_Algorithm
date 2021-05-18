# 입력 예시
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]
indegree = [0] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

stack = []
result = []

for i in range(1, v+1):
    if indegree[i] == 0:
        stack.append(i)

def dfs():
    while stack:
        x = stack.pop()
        result.append(x)
        for y in edges[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                stack.append(y)

dfs()
print(*result)
# 1 5 2 6 3 4 7