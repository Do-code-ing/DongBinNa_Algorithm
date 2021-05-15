# <문제> 정렬된 배열에서 특정 수의 개수 구하기: 문제 설명
# N개의 원소를 포함고 있는 수열이 오름차순으로 정렬되어 있습니다.
# 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
# 예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면,
# 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
# 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받습니다.
# 값이 x인 원소가 하나도 없다면 -1을 출력합니다.

n, x = 7, 2
arr = [1, 1, 2, 2, 2, 2, 3]

from collections import Counter

a = Counter(arr)
if a[x]:
    print(a[x])
else:
    print(-1)

n, x = 7, 2
arr = [1, 1, 2, 2, 2, 2, 3]

from bisect import *

left = bisect_left(arr, x)
right = bisect_right(arr, x)
if left == len(arr):
    print(-1)
else:
    print(right-left)

# [문제 해결 아이디어]
# 시간 복잡도 O(logN)으로 동작하는 알고리즘을 요구하고 있습니다.
#   - 일반적인 선형탐색으로는 시간 초과 판정을 받습니다.
#   - 하지만 데이터가 정렬되어 있기 때문에 이진 탐색을 수행할 수 있습니다.
# 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제를 해결할 수 있습니다.

n, x = 7, 2
arr = [1, 1, 2, 2, 2, 2, 3]

from bisect import *

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

count = count_by_range(arr, x, x)

if count:
    print(count)
else:
    print(-1)