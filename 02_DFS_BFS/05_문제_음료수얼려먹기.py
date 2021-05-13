# <문제> 음료수 얼려 먹기: 문제 설명
# N * M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
# 다음의 4 * 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

# 00110
# 00011
# 11111
# 00000

from collections import deque

n, m = 4, 5
board = [
    "00110",
    "00011",
    "11111",
    "00000"
]
# visited = [[False] * m for _ in range(n)]
# from collections import deque

# def icing(board, x, y , visited):
#     queue = deque([x,y])
#     visited[x][y] = True
#     while queue:
#         v = queue.popleft()
#         w = queue.popleft()
#         for i in board[v][w]:
#             if not visited[i]:
#                 queue.append

# [문제 해결 아이디어]
# 이 문제는 DFS 혹은 BFS로 해결할 수 있습니다.
# 일단 앞에서 배운대로 얼음을 얼릴 수 있는 공간이 상, 하, 좌, 우로 연결되어 있다고 표현할 수 있으므로
# 그래프 형태로 모델링 할 수 있습니다. 다음과 같이 3 * 3 크기의 얼음틀이 있다고 가정하고 생각해 봅시다.

# 0 0 1
# 0 1 0
# 1 0 1

# DFS를 활용하는 알고리즘은 다음과 같습니다.
#   1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에
#       주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문합니다.
#   2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴포면서 방문을 진행하는 과정을 반복하면,
#       연결된 모든 지점을 방문할 수 있습니다.
#   3. 모든 노드에 대하여 1 ~ 2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트합니다.

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 좌표값이 범위를 벗어나면 False
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0: # 즉, 좌표값이 0이면
        graph[x][y] = 1 # 1로 바꿔주고, 방문처리 해주고
        dfs(x-1, y) # 상하좌우에 대해서도 탐색
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True # 방문처리가 됐음을 의미
    return False

n, m = 4, 5
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True: # 방문처리가 되었다면
            result += 1
print(result)

# BFS로 풀어보자

n, m = 4, 5
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]
result = 0
# BFS 함수
def bfs(graph, x, y):
    q = deque() # 큐 구조 형성하고 초기 좌표값 입력
    q.append(x)
    q.append(y)
    while q: # 탐색을 마치기 전까지
        ax, ay = q.popleft(), q.popleft() # q에서 row, column 값 받아오고 
        graph[ax][ay] = 1 # 방문 처리
        dx = [-1, 1, 0, 0] # 방향 벡터 설정
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = ax+dx[i] # 방향 벡터에 따라 이동
            ny = ay+dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m: # 규격을 벗어나면 넘어가기
                pass
            elif graph[nx][ny] == 0: # 규격안에 있고, 해당 좌표가 0이라면,
                q.append(nx) # q에 좌표값 추가
                q.append(ny)
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: # 현재 좌표에서 얼음을 찾았다면,
            result += 1 # 찾았다고 처리하고
            bfs(graph, i, j) # 찾은 얼음과 붙어있는 얼음들 제거
print(result)