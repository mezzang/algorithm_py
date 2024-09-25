MOD = 10000000
def poly(n):
    dp = [[0] * (i+1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for first in range(1, i + 1):
            if i == first:
                dp[i][first] = 1
            else:
                ret = 0
                for second in range(1, i - first + 1):
                    ret = (ret + (second + first - 1) * dp[i - first][second]) % MOD
                dp[i][first] = ret
    return sum(dp[n]) % MOD

        
for _ in range(int(input())):
    n = int(input())
    ret = 0
    
    print(poly(n))