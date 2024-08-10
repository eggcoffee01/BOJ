if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)

    INF = 100000000
    input = sys.stdin.readline
    n = int(input())
    ## matrix는 게임판, 칸별로 갈 수 있는 거리를 가지고 있다.
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    ## dp는 해당 구조상 해당 칸으로 몇번 올 수 있는지를 저장한다.
    dp = [[0 for _ in range(n)]for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0 or matrix[i][j] == 0:
                continue
            jump = matrix[i][j]
            if i + jump <= n-1:
                dp[i+jump][j] += dp[i][j]
            if j + jump <= n-1:
                dp[i][jump+j] += dp[i][j]
    print(dp[n-1][n-1])
            
    
    