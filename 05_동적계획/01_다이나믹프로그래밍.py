# 다이나믹 프로그래밍

# 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법입니다.
# 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 합니다.
# 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운, 바텀업)으로 구성됩니다.

# 동적 계획법이라고도 부릅니다.
# 일반적인 프로그래밍 분야에서의 동적(Dynamic)이란 어떤 의미를 가질까요?
#   - 자료구조에서 동적 할당(Dynamic Allocation)은
#     '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'을 의미합니다.
#   - 반면에 다이나믹 프로그래밍에서 '다이나믹'은 별다른 의미 없이 사용된 단어입니다.


# 다이나믹 프로그래밍의 조건
# 다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있습니다.
#   1. 최적 부분 구조(Optimal Substructure)
#       - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있습니다.
#   2. 중복되는 부분 문제(Overlapping Subproblem)
#       - 동일한 작은 문제를 반복하여 해결해야 합니다.


# 피보나치 수열
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 점화식이란 인접한 항들 사이의 관계식을 의미합니다.
# 피보나치 수열을 점화식으로 표현하면 다음과 같습니다.
# an = an-1 + an-2, a1 = 1, a2 = 1

# [피보나치 수열: 단순 재귀 소스코드]

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# [피보나치 수열의 시간 복잡도 분석]
# 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 됩니다.
# 중복되는 부분이 생기기 때문입니다.
# 피보나치 수열의 시간 복잡도는 다음과 같습니다.
#   - 세타 표기법: 세타(1.618..^n)
#   - 빅오 표기법: O(2^n)
# 빅오 표기법을 기준으로 f(30)을 계산하기 위해 약 10억가량의 연산을 수행해야 합니다.
# 그렇다면 f(100)을 계사하기 위해 얼마나 많은 연산을 수행해야 할까요?


# 피보나치 수열의 효율적인 해법: 다이나믹 프로그래밍
# 다이나믹 프로그래밍의 사용 조건을 만족하는지 확인합니다.
#   1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있습니다.
#   2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결합니다.
# 피보나치 수열은 다이나믹 프로그래밍의 사용 조건을 만족합니다.

# 메모이제이션(Memoization) : 탑다운, 하향식
# 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나입니다.
# 한 번 계산한 결과를 메모리 공간에 메모하는 기법입니다.
#   - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옵니다.
#   - 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 합니다.

# 탑다운 VS 바텀업
# 탑다운(메모이제이션) 방식은 하향식이라고도 하며 바텀업 방식은 상향식이라고도 합니다.
# 다이나믹 프로그래밍의 전형적인 형태는 바텀업 방식입니다.
#   - 결과 저장용 리스트는 DP 테이블이라고 부릅니다.
# 엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미합니다.
#   - 따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아닙니다.
#   - 한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있습니다.

# [피보나치 수열: 탑다운 다이나믹 프로그래밍 소스코드]

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100
# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
        # 이미 게산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# [피보나치 수열: 바텀업 다이나믹 프로그래밍 소스코드]

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100
# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99
# 피보나치 함수 반복문으로 구현(바텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

# [피보나치 수열: 메모이제이션 동작 분석]
# 메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 O(N)입니다.

d = [0] * 100
def fibo(x):
    print("f(" + str(x) + ")", end=" ")
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

fibo(6)
print()


# 다이나믹 프로그래밍 VS 분할 정복

# 다이나믹 프로그래밍과 분할 정복은 모두 최적 부분 구조를 가질 때 사용할 수 있습니다.
#   - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황
# 다이나믹 프로그래밍과 분할 정복의 차이점은 부분 문제의 중복입니다.
#   - 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복됩니다.
#   - 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않습니다.


# 다이나믹 프로그래밍 문제에 접근하는 방법
# 주어진 문제가 다이나믹 프로그래밍 유형임을 파악하는 것이 중요합니다.
# 가장 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토할 수 있습니다.
#   - 다른 알고리즘으로 풀이 방법이 떠오르지 않으면 다이나믹 프로그래밍을 고려해 봅시다.
# 일단 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤에 (탑다운) 작은 문제에서 구한 답이
#   큰 문제에서 그대로 사용될 수 있으면, 코드를 개선하는 방법을 사용할 수 있습니다.
# 일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 출제되는 경우가 많습니다.


# <문제> 개미 전사: 문제 설명
# 개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 합니다.
# 메뚜기 마을에는 여러 개의 식량창고가 있는데 식량창고는 일직선으로 이어져 있습니다.
# 각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여
#   식량을 빼앗을 예정입니다.
# 이때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있습니다.
# 따라서 개미 전사가 정찰병에게 틀기지 않고 식량창고를 약탈하기 위해서는
#   최소한 한 칸 이상 떨어진 식량창고를 약탈해야 합니다.
# 예를 들어 식량창고 4개가 다음과 같이 존재한다고 가정합시다.
# 1, 3, 1, 5
# 이때 개미 전사는 두 번째 식량창고와 네 번째 식량창고를 선택했을 때 최댓값이 총 8개의 식량을 빼앗을 수 있습니다.
# 개미 전사는 식량창고가 이렇게 일직선상일 때 최대한 많은 식량을 얻기를 원합니다.
# 개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하세요.

n = 4
arr = [1, 3, 1, 5]

# [문제 해결 아이디어]
# 예시를 확인해 봅시다. N = 4일 때, 다음과 같은 경우들이 존재할 수 있습니다.
#   - 식량을 선택할 수 있는 경우의 수는 다음과 같이 8가지입니다.
#   - 7번째 경우에서 8만큼의 식량을 얻을 수 있으므로 최적의 해는 8입니다.

# ai = i번째 식량창고까지의 최적의 해(얻을 수 있는 식량의 최댓값)
#   - 이렇게 정의한다면 다이나믹 프로그래밍을 적용할 수 있습니다.
# DP 테이블의 값 : a0 = 1, a1 = 3, a2 = 3, a3 = 8

# ai = i번째 식량창고까지의 최적의 해(얻을 수 있는 식량의 최댓값)
# ki = i번째 식량창고에 있는 식량의 양
# 점화식은 다음과 같습니다.
#       ai = max(ai-1, ai-2 + ki)
# 한 칸 이상 떨어진 식량창고는 항상 털 수 있으므로 (i-3)번째 이하는 고려할 필요가 없습니다.

n = 4
array = [1, 3, 1, 5]
d = [0] * n
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])


# <문제> 1로 만들기: 문제 설명
# 정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지입니다.
#   1. X가 5로 나누어 떨어지면, 5로 나눕니다.
#   2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.
#   3. X가 2로 나누어 떨어지면, 2로 나눕니다.
#   4. X에서 1을 뺍니다.
# 정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 값을 1로 만들고자 합니다.
# 연산을 사용하는 횟수의 최솟값을 출력하세요.
# 예를 들어 정수가 26이며 다음과 같이 계산해서 3번의 연산이 최솟값입니다.
# 26 -> 25 -> 5 -> 1

x = 26
d = [0] * 30001
for i in range(1, x):
    d[i] = 1

# [문제 해결 아이디어]
# 피보나치 수열 문제를 도식화한 것처럼 함수가 호출되는 과정을 그림으로 그려보면 다음과 같습니다.
#    - 최적 부분 구조와 중복되는 부분 문제를 만족합니다.

# ai = i를 1로 만들기 위한 최소 연산 횟수
# 점화식은 다음과 같습니다.
#       ai = min(ai-1, ai/2, ai/3, ai/5) + 1
# 단, 1을 빼는 연산을 제외하고는 해당 수로 나누어떨어질 때에 한해 점화식을 적용할 수 있습니다.

x = 26
d = [0] * (x+1)
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])


# <문제> 효율적인 화폐 구성: 문제 설명
# N가지 종류의 화폐가 있습니다.
# 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 합니다.
# 이때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.
# 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 최소한의 화폐 개수입니다.
# M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.

n, m = 2, 15
coin = [2, 3]

# [문제 해결 아이디어]
# ai = 금액 i를 만들 수 있는 최소한의 화폐 개수
# k = 각 화폐의 단위
# 점화식: 각 화폐 단위인 k를 하나씩 확인하며
#   - ai-k를 만드는 방법이 존재하는 경우, ai = min(ai, ai-k + 1)
#   - ai-k를 만드는 방법이 존재하지 않는 경우, ai = INF

n, m = 2, 15
array = [2, 3]
INF = float("inf")
d = [INF] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != INF: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == INF:
    print(-1)
else:
    print(d[m])


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


# <문제> 병사 배치하기: 문제 설명
# N명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유하고 있습니다.
# 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 합니다.
# 다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 합니다.
# 또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다.
# 그러면서도 남아 있는 병사의 수가 최대가 되도록 하고 싶습니다.

from bisect import *

n = 7
arr = list(reversed([15, 11, 4, 8, 5, 2, 4]))
result = [0]
for i in arr:
    if i > result[-1]:
        result.append(i)
    else:
        result[bisect_left(result, i)] = i
    print(i, result)
print(n - (len(result)-1))


# [문제 해결 아이디어]
# 이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)로
#   알려진 전형적인 다이나믹 프로그래밍 문제의 아이디어와 같습니다.
# 예를 들어 하나의 수열 array = {4,2,5,8,4,11,15}이 있다고 합시다.
#   - 이 수열의 가장 긴 증가하는 부분 수열은 {4,5,8,11,15}입니다.
# 본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제로 치환할 수 있으므로, LIS 알고리즘을 조금 수정하여
#   적용함으로써 정답을 도출할 수 있습니다.

# 가장 긴 증가하는 부분 수열 (LIS) 알고리즘을 확인해 봅시다.
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 점화식은 다음과 같습니다.
#       모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]

# 가장 먼저 입력받은 병사 정보의 순서를 뒤집습니다.
# 가장 긴 증갛는 부분 수열 (LIS) 알고리즘을 수행하여 정답을 도출합니다.

n = 7
array = [15, 11, 4, 8, 5, 2, 4]
array.reverse()
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))