from sys import stdin
input = stdin.readline

def solution():
    t = input().rstrip()
    p = input().rstrip()
    n = len(t)
    m = len(p)

    # pattern 에서 접두사와 접미사의 최대 공통 구간을 찾는다.
    dp = [0] * m
    j = 0
    for i in range(1, m):
        # 접두사와 접미사가 일치하지 않는다면, 일치 이전 인덱스로 돌아간다.
        while j > 0 and p[i] != p[j]:
            j = dp[j-1]

        # 일치한다면, 기록하고, 다음 인덱스 탐색
        if p[i] == p[j]:
            j += 1
            dp[i] = j
    
    answer = 0 # 최대 일치 문자열 수
    result = [] # 어느 인덱스부터 일치하는 지 저장
    j = 0
    for i in range(n):
        while j > 0 and t[i] != p[j]:
            j = dp[j-1]
        
        # 일치한다면
        if t[i] == p[j]:
            # 만약 모든 부분이 일치했다면,
            if j == m-1:
                answer += 1
                result.append(i-m+2)
                j = dp[j]
            else:
                j += 1
    
    print(answer)
    print(" ".join(map(str, result)))

solution()