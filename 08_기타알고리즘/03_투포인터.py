# [투 포인터 (Two Pointer)]

# 투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘을 의미합나디.
# 흔히 2, 3, 4, 5, 6, 7번 학생을 지목해야 할 때 간단히 '2번부터 7번까지의 학생'이라고 부르곤 합니다.
# 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 시작점과 끝점 2개의 점으로 접근할 데이터의 범위를 표현할 수 있습니다.


# [특정한 합을 가지는 부분 연속 수열 찾기: 문제 설명]
# N개의 자연수로 구성된 수열이 있습니다.
# 합이 M인 부분 연속 수열의 개수를 구해보세요.
# 수행 시간 제한은 O(N)입니다.

array = [1, 2, 3, 2, 5]
M = 5
# 2 3
# 3 2
# 5
# 총 세가지의 경우가 있다.
# 완전 탐색으로 풀게 될 경우 O(N^2)의 시간이 소요된다.

# [문제 해결 아이디어]
# 투 포인터를 활용하여 다음과 같은 알고리즘으로 문제를 해결할 수 있습니다.
#   1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.ㄴ
#   2. 현재 부분 합이 M과 같다면, 카운트한다.
#   3. 현재 부분 합이 M보다 작다면, end를 1 증가시킨다.
#   4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다.
#   5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.


# [특정한 합을 가지는 부분 연속 수열 찾기: 코드 예시]

n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)

# 투 포인터 알고리즘은 다양한 방법으로 구현할 수 있는데,
# 문제마다 효율적인 구현이 다를 수 있다.