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