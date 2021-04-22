# N개의 정수로 구성된 수열이 있습니다.
# M개의 쿼리 정보가 주어집니다.
#   각 쿼리는 L과 R로 구성됩니다.
#   [L,R]구간에 해당하는 데이터들의 합을 모두 구해보세요.

N = [10,20,30,40,50]
M = int(input())
for _ in range(M):
    L, R = map(int, input().split())
    print(sum(N[L-1:R])) # or list에 저장, list.append(sum(N[L-1:R]))

# 구간 합 빠르게 계산하기
# [문제 설명]
# 아래와 같이 N개의 정수로 구성된 수열이 있습니다.
# M개의 쿼리 정보가 주어집니다.
#   각 쿼리는 L과 R로 구성됩니다.
#   [L,R]구간에 해당하는 데이터들의 합을 모두 구하는 문제입니다.
# 시간 제한: O(N+M)

# [문제 해결 방법]
# 접두사 합(Prefix Sum)

# [Prefix Sum을 활용한 알고리즘 설명]
# 1. Prefix Sum을 계산하여 배열 P에 저장한다.
# 2. 매 M개의 쿼리 정보를 확인할 때, 구간 합은 P[R]-R[L-1]

#      [10, 20, 30, 40, 50]
#           Prefix Sum 계산
# [0, 10, 30, 60, 100, 150]

# ex) L = 1, R = 3 -> P[3]-P[1-1] = 60

n = 5
data = [10,20,30,40,50]
summary = 0
prefix_sum = [0]
for i in data:
    summary += i
    prefix_sum.append(summary)
left = 3
right = 4
print(prefix_sum[right]-prefix_sum[left-1])