# 그래프 탐색 알고리즘: DFS/BFS

# 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말합니다.
# 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있습니다.
# 자주 등장하는 유형이므로 반드시 숙지해야 합니다.


# [스택 자료구조]
# 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조입니다.
# 입구와 출구가 동일한 형태로 스택을 시각화할 수 있습니다.
# DFS 알고리즘뿐 만아니라 다양한 알고리즘에서 사용된다.

# 스택 동작 예시
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력


# [큐 자료구조]
# 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조입니다.
# 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있습니다.

# 큐 동작 예시
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

# 리스트를 사용하여 해도 되지만, 시간복잡도가 조금 더 걸리기에
# 덱 라이브러리 사용이 좋다.
from collections import deque

queue = deque()

queue.append(5)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
print(queue)
queue.append(4)
print(queue)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
print(list(queue))

# 스택 자료구조는 들어온 순서에서 마지막 것만 제거하면 되기 때문에 자료의 인덱스의 변화가 없다.
# 그렇기에 list를 사용하여 스택 구조를 만들어 사용해도 된다.
# 그러나 큐 자료구조에서는 제일 먼저 들어온 것을 제거하기 때문에 리스트로 자료구조를 만들 경우,
# 인덱스 변화가 일어나기 때문에 시간 복잡도가 조금 더 걸린다.
# 그렇기에 덱 라이브러리를 이용하여 popleft를 하는 것이 시간 복잡도 측면에서 좋다.
# (리스트에서 pop과 덱에서 popleft의 시간복잡도는 같은듯하다.)


# [재귀 함수]
# 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미합니다.
# 단순 형태의 재귀 함수 예제
def aaa():
    print("본인을 호출했어요")
    aaa()
# aaa()
# RecursionError: maximum recursion depth exceeded while calling a Python object
# 컴퓨터 메모리에 스택과 같이 함수가 쌓여, 빠르게 메모리가 가득차서 문제가 발생할 수 있어, 제한이 있다.
# 그렇기에 재귀 제한을 느슨하게 만드는 방법을 사용하거나, 스택 객체를 따로 만들어서 그것을 이용하는 방법도 있다.

# 재귀 함수를 문제 풀이에 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 합니다.
# 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있습니다.
#   - 종료 조건을 포함한 재귀 함수 예제
def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i+1,"번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(i, "번째 재귀함수를 종료합니다.")
# recursive_function(1)
# 스택에 데이터를 넣은 것처럼 사용하는 결과를 보여준다.

# 팩토리얼 구현 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print("반복적으로 구현:", factorial_iterative(5))
print("재귀적으로 구현:", factorial_recursive(5))

# 최대공약수 계산(유클리드 호제법) 예제
# 두 개의 자연수에 대한 최대 공약수를 구하는 대표적인 알고리즘
# 유클리드 호제법
#   - 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 합시다.
#   - 이때 A와 B의 최대공약수는 B와 R의 최대 공약수와 같습니다.
# 이것을 재귀 함수로 작성할 수 있습니다.
def gcd(a, b):
    # a, b = max(a,b), min(a,b) # 혹시몰라 정렬
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b) # 이 과정에서 알아서 큰수와 작은수로 정렬됨
print(gcd(12, 20))

# 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있습니다.
#   - 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수 있으므로 신중하게 사용해야 합니다.
# 모든 재귀 함수는 반복문을 이용하여 동일하 기능을 구현할 수 있습니다.
# 재귀 함수가 반복문 보다 유리한 경우도 있고 불리한 경우도 있습니다.
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓입니다.
#   - 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많습니다.
# DFS에서는 재귀 함수를 이용한다.


# [DFS] (Depth-First Search)
# DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘입니다.
# DFS는 스택 자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
#   1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
#   2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고
#       방문 처리합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
#   3. 더 이상 2번 과정을 수행할 수 없을 때까지 반복합니다.

# DFS 소스코드 예제

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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
visited = [False] * 9 # 인덱스 0을 처리하지 않기 위해서, 하나 더 표현
# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
print()


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


# <문제> 음료수 얼려 먹기: 문제 설명
# N * M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
# 다음의 4 * 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

# 00110
# 00011
# 11111
# 00000

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


# <문제> 미로 탈출: 문제 설명
# 동빈이는 N * M 크기의 직사각형 형태의 미로에 갇혔습니다.
# 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
# 동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
# 이때 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하세요.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

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