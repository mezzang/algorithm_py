def trianglepath(y, x):
    dp = T[n-1][:]

    for i in range(n-2, -1, -1):
        for j in range(i + 1):
            dp[j]= T[i][j] + max(dp[j], dp[j + 1])
    return dp[0]

for _ in range(int (input())):
    n = int(input())
    T = [list(map(int, input().split())) for _ in range(n)]
    print(trianglepath(0,0))
  
    