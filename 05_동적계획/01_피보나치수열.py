# [피보나치 수열]

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


# [피보나치 수열의 효율적인 해법: 다이나믹 프로그래밍]

# 다이나믹 프로그래밍의 사용 조건을 만족하는지 확인합니다.
#   1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있습니다.
#   2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결합니다.
# 피보나치 수열은 다이나믹 프로그래밍의 사용 조건을 만족합니다.


# [메모이제이션(Memoization) : 탑다운, 하향식]

# 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나입니다.
# 한 번 계산한 결과를 메모리 공간에 메모하는 기법입니다.
#   - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옵니다.
#   - 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 합니다.

# [탑다운 VS 바텀업]

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