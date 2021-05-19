# <문제> 금광: 문제 설명
# n * m 크기의 금광이 있습니다.
# 금광은 1 * 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다.
# 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.
# 이후에 m-1버에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     arr = []
#     temp = list(map(int, input().split()))
#     for i in range(0, n*m, m):
#         arr.append(temp[i:i+m])
    
n, m = 3, 4
dp = [
    [1, 3, 3, 2],
    [2, 1, 4, 1],
    [0, 6, 4, 7],
]

# for i in range(n):
#     for j in range(m):
#         if 0 <= i-1 and 0 <= j-1 and i+1 <= n:
#             dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

# result = []
# for i in range(n):
#     result.append(dp[i][-1])

# print(max(result))

# [문제 해결 아이디어]
# 금광의 모든 위치에 대하여 다음의 세가지만 고려하면 됩니다.
#   1. 왼쪽 위에서 오는 경우
#   2. 왼쪽 아래에서 오는 경우
#   3. 왼쪽에서 오는 경우
# 세 가지 경우 중에서 가장 많은 금을 가지고 있는 경우를 테이블에 갱신해주어 문제를 해결합니다.

# array[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j] = i행 j열까지의 최적의 해(얻을 수 있는 금의 최댓값)
# 점화식은 다음과 같습니다.
#       dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
# 이때 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크해야 합니다.
# 편의상 초기 데이터를 담는 변수 array를 사용하지 않아도 됩니다.
#   - 바로 DP 테이블에 초기 데이터를 담아서 다이나믹 프로그래밍을 적용할 수 있습니다.

n, m = 3, 4
dp = [
    [1, 3, 3, 2],
    [2, 1, 4, 1],
    [0, 6, 4, 7],
]

for j in range(1, m): # 각 열에서
    for i in range(n): # 각 행별로 체크
        # 왼쪽 위에서 오는 경우
        if i == 0:
            left_up = 0
        else:
            left_up = dp[i-1][j-1]
        # 왼쪽 아래에서 오는 경우
        if i == n-1:
            left_down = 0
        else:
            left_down = dp[i+1][j-1]
        # 왼쪽에서 오는 경우
        left = dp[i][j-1]
        dp[i][j] = dp[i][j] + max(left_up, left_down, left)
result = 0
for i in range(n):
    result = max(result, dp[i][m-1])
print(result)