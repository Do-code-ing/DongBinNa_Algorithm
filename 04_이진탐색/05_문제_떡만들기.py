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