# 이진 탐색 알고리즘


# 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진 탐색: 정렬되어 잇는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
#   - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.


# [이진 탐색의 시간 복잡도]
# 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2N에 비례합니다.
# 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개가량의 데이터만 남습니다.
#   - 2단계를 거치면 8개가량의 데이터만 남습니다.
#   - 3단계를 거치면 4개가량의 데이터만 남습니다.
# 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장합니다.

# 이진 탐색 소스코드: 재귀적 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

n, target = 10, 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

# 이진 탐색 소스코드: 반복문 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = 10, 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


# [파이썬 이진 탐색 라이브러리]

# bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

from bisect import *

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# 값이 특정 범위에 속하는 데이터 개수 구하기

from bisect import *

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))
# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))


# [파라메트릭 서치] (Parametric Search)
# 파라메트릭 서치란 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법입니다.
#   - 예시: 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 일반적으로 코딩 테스트에서 파라메트릭 서치문제는 이진 탐색을 이용하여 해결할 수 있습니다.


# <문제> 떡볶이 떡 만들기: 문제 설명
# 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했습니다.
# 오늘은 떡볶이 떡을 만드는 날입니다.
# 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않습니다.
# 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춥니다.

# 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단합니다.
# 높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다.

# 예를 들어, 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면
# 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것입니다.
# 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm입니다.
# 손님은 6cm만큼의 길이를 가져갑니다.

# 손님이 왔을 때 요청한 총 길이가 M일 때
# 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요.

n, m = 4, 6
arr = [19, 15, 10, 17]

def cut(arr, start, end):
    if start >= end:
        return
    mid = (start+end) // 2
    temp = 0
    for i in arr:
        if i > mid:
            temp += i - mid
    if temp == m:
        print(mid)
    elif temp > m:
        cut(arr, mid+1, end)
    else:
        cut(arr, start, mid-1)

cut(arr, 0, max(arr))

n, m = 4, 6
arr = [19, 15, 10, 17]

start = 0
end = max(arr)
while True: # while start <= end:
    total = 0
    mid = (start+end) // 2
    for i in arr:
        if i > mid:
            total += i - mid
    if total == m:
        break
    if total < m:
        end = mid - 1
    else:
        start = mid + 1

print(mid)

# [문제 해결 아이디어]
# 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정하면 됩니다.
# '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤에
# 조건의 만족 여부('예' 혹은 '아니오')에 따라서 탐색 범위를 좁혀서 해결할 수 있습니다.
# 절단기의 높이는 0부터 10억까지의 정수 중 하나입니다.
#   - 이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 합니다.
# 문제에서 제시된 예시를 통해 그림으로 이해해 봅시다.

# 중간점의 값은 시간이 지날수록 '최적화된 값'이 되기 때문에,
# 과정을 반복하면서 얻을 수 있는 떡의 길이 합이 필요한 떡의 길이보다 크거나 같을 때마다 중간점의 값을 기록하면 됩니다.

n, m = 4, 6
arr = [19, 15, 10, 17]
# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(arr)
# 이진 탐색 수행 (반복적)
result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in arr:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x -mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)

###################### 이게 제일 시간 복잡도가 낮음

n, m = 4, 6
arr = [19, 15, 10, 17]

def cut(arr, mid):
    total = 0
    for x in arr:
        if x > mid:
            total += x - mid
    return total

start = 0
end = max(arr)

while start <= end:
    mid = (start+end) // 2
    total = cut(arr, mid)
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)

######################

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