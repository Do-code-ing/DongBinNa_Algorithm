# 구현

# 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
# 모든 문제가 구현을 필요로 하지만, 코딩테스트에서는 다음과 같다.

# 구현 유형의 문제란,
#   - 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 칭합니다.

# 구현 유형의 예시
#   - 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
#   - 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
#   - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
#   - 적절한 라이브러리를 찾아서 사용해야 하는 문제

# 알고리즘 문제에서 2차원 공간 행렬(Matrix)의 의미로 사용됩니다.

data = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
]

# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됩니다.

#    동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 동서로 이동할 때는 열(y) 좌표를, 남북으로 이동할 때는 행(x) 좌표를 수정하면 된다.

# 현재 위치가 (2, 2) 일 때,
x, y = 2, 2
# 다음 위치
for i in range(4):
    nx = x + dx[i] # i에 이동하고 싶은 방향 입력
    ny = y + dy[i]
    # print(nx, ny)


# <문제> 상하좌우: 문제 설명
# 여행가 A는 N * N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 * 1 크기의 정사각형으로 나누어져 있습니다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다.
# 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.

# 계획서에는 하나의 줄에 띄어씌기를 기준으로 L, R, U, D중 하나의 문자가 반복적으로 적혀 있습니다.
# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동

# 이때 여행가 A가 N * N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다.
# 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시됩니다.
# 다음은 N = 5인 지도와 계획서 입니다.

n = 5
move = ["R", "R", "R", "U", "D"," D"]
x, y = 1, 1
for m in move:
    if m == "L":
        if y != 1:
            y -= 1
    elif m == "R":
        if y != 5:
            y += 1
    elif m == "U":
        if x != 1:
            x -= 1
    else:
        if x != 5:
            x += 1
print(x, y)

# [문제 해결 아이디어]
# 요구사항대로 충실히 구현하면 되는 문제
# 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로도 분류가 된다.
#   - 다만, 알고리즘 교재나 문제 풀이 사이트에 따라서 다르게 부를 수 있으므로,
#   - 코딩 테스트에서의 시뮬레이션 유형, 구현 유형, 완전 탐색 유형은 서로 유사한 점이 많다 정도로만 기억합시다.

# 해답
n = 5
plans = ["R", "R", "R", "U", "D", "D"]
x, y = 1, 1
# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)


# <문제> 시각: 문제설명
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
#   - 00시 00분 03초
#   - 00시 13분 30초
# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각입니다.
#   - 00시 02분 55초
#   - 01시 27분 45초

n = 0
answer = 0
for s in range(1, 60):
    for m in range(1, 60):
        for t in range(n+1):
            if "3" in str(t)+str(m)+str(s):
                answer += 1
print(answer)

# [문제 해결 아이디어]
# 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제입니다. (즉, 전형적인 완전 탐색 문제)
# 하루는 86,400초이므로, 00시 00분 00초부터 23시 59분 59초까지의 모든 경우는 86,400가지입니다.
#   24 * 60 * 60 = 86,400
# 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면 됩니다.
# 이러한 유형은 완전 탐색(Brute Forcing)문제 유형이라고 불립니다.


# <문제> 왕실의 나이트: 문제 설명
# 왕실 정원은 체스판과 같은 8 * 8 좌표 평면입니다.
# 왕실 정원의 특정한 한 칸에 나이트가 서 있습니다.
# 나이트는 말을 타고 있기 때문에 이동할 때 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다.
# 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
#   1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
#   2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 행은 1-8, 열은 a-h로 표현된다.
# 입력이 a1과 같이 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력하시오.

n = "d4"
m = 8
st = ["a","b","c","d",'e','f','g','h']
num = [1,2,3,4,5,6,7,8]
count = 0
x, y = 0, 0
for i in range(len(st)):
    if n[0] in st[i]:
        y = num[i]
        break
x = int(n[1])
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx >= m or ny >= m:
        continue
    else:
        count += 1
print(count)

# [문제 해결 아이디어]
# 요구 사항대로 충실히 구현하면 되는 문제이다.
# 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능하지 확인합니다.
#   - 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의합니다.

# 해답
# 현재 나이트의 위치 입력받기
n = "d4"
row = int(n[1])
column = int(ord(n[0])) - int(ord("a")) + 1
# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)


# <문제> 문자열 재정렬: 문제 설명
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

n = "K1KA5CB7"
n = "AJKDLSI412K4JSJ9D"
answer = ""
num = 0
n = sorted(n)
for c in n:
    if c.isalpha():
        answer += c
    else:
        num += int(c)
if num != 0:
    answer += str(num)
print(answer)

# [문제 해결 아이디어]
# 요구 사항대로 충실히 구현
# 문자열이 입력되었을 때 문자를 하나씩 확인합니다.
#   - 숫자인 경우 따로 합계를 계산합니다.
#   - 알파벳의 경우 별도의 리스트에 저장합니다.
# 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답입니다.

# 해답
data = "K1KA5CB7"
data = "AJKDLSI412K4JSJ9D"
result = []
value = 0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0:
    result.append(str(value))
print("".join(result))