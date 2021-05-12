# <문제> 1이 될 때까지: 문제 설명
# 수 N이 1이 될 떄까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

N = 25
K = 3
count = 0
while N != 1:
    if N % K != 0:
        N -= 1
        count += 1
    else:
        N /= K
        count += 1
print(count)

# [정당성 분석]
# N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄일 수 있습니다.
# 다시 말해 K가 2 이상이기만 하면, K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있습니다.
#   - 또한 N은 항상 1에 도달하게 됩니다.(최적의 해 성립)

# 해답
N = 25
K = 3
result = 0
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N//K) * K
    result += (N-target)
    N = target
    # N이 K보다 작을 때(더 이상 나눌수 없을 때) 반복문 탈출
    if N < K:
        break
    result += 1
    N //= K
result += (N-1)
print(result)