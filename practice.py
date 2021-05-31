import sys
input = sys.stdin.readline
        
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    dp = [[0] * (n) for _ in range(n)]
    for diag in range(n):
        for i in range(n):
            j = i + diag
            
            if j >= n:
                break
            
            if i == j:
                dp[i][j] = 1
                continue
                
            if j - i == 1:
                if arr[i] == arr[j]:
                    dp[i][j] = 1
                    continue
            
            if arr[i] == arr[j] and dp[i+1][j-1]:
                dp[i][j] = 1
    
    for _ in range(m):
        s, e = map(int, input().split())
        print(dp[s-1][e-1])

solution()