# 아래와 같이 자연수로 구성된 수열 k가 있습니다.
# 합이 5인 부분 연속 수열의 개수를 구해보세요.

k = [1,2,3,2,5]
answer = 0
for i in range(len(k)):
    temp = k[i]
    j = i+1
    while temp <= 5:
        if temp < 5:
            temp += k[j]
            j += 1
        elif temp == 5:
            answer += 1
            break
print(answer)

# 특정한 합을 가지는 부분 연속 수열 찾기

# [문제설명]
# N개의 자연수로 구성된 수열이 있습니다.
# 합이 M인 부분 연속 수열의 개수를 구해보세요.
# 시간 제한: O(N)

# [문제 해결 방법]
# 투 포인터 방법: 리스트에 순차적으로 접근해야 할 때 두 개의 점을 이용해 위치를 기록하면서 처리하는 기법

# [투 포인터를 활용한 알고리즘 설명]
# 1. 시작점(start)과 끝점(end)이 첫 번째 원소 인덱스(0)를 가리키도록 한다.
# 2. 현재 부분 합이 M과 같다면, 카운트한다.
# 3. 현재 부분 합이 M보다 작거나 같다면, end를 1 증가시킨다.
# 4. 현재 부분 합이 M보다 크다면, start를 1 증가시킨다.
# 5. 모든 경우를 확인할 때까지 2~4를 반복한다.

# 데이터의 개수 N과 부분 연속 수열의 합 M을 입력 받기
n, m = 5, 5
data = [1,2,3,2,5]

result = 0
summary = 0
end = 0
# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동 시키기
    while summary < m and end < n:
        summary += data[end]
        end += 1
    # 부분 합이 m일 때 카운트 증가
    if summary == m:
        result += 1
    summary -= data[start]
print(result)