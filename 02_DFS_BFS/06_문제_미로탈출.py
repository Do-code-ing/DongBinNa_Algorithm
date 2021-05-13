# <문제> 미로 탈출: 문제 설명
# 동빈이는 N * M 크기의 직사각형 형태의 미로에 갇혔습니다.
# 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
# 동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
# 이때 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하세요.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

from collections import deque

n, m = 5, 6
maze = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                pass
            elif maze[nx][ny] == 1:
                maze[nx][ny] += maze[ax][ay]
                q.append((nx, ny))
    return maze[n-1][m-1]
print(bfs(0, 0))


# [문제 해결 아이디어]
# BFS는 시작 지점에서 가장 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색합니다.
# 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일합니다.
#   따라서 (1, 1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있습니다.