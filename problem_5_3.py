MAX = 2000000001

def make_length(n, S):
    dp = [1] * (n+1)
    for i in range(n-1, -2, -1):
        for j in range(i + 1, n):
            if S[i] < S[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def make_count(n, S):
    dp = [1] * (n + 1)
    for i in range(n - 1, -2, -1):
        if dp_len[i] == 1:
            dp[i] = 1
        else:
            ret = 0
            for j in range(i + 1, n):
                if S[i] < S[j] and dp_len[i] == dp_len[j] + 1:
                    ret = min(MAX, ret + dp[j])
            dp[i] = ret
    return dp

def reconstruct(start, skip, result):
    global n, S, dp_len, dp_cnt
    result.append(S[start])
    
    followers = []
    for next in range(start + 1, n):
        if start == -1 or (S[start] < S[next] and dp_len[start] == dp_len[next] + 1):
            followers.append((S[next], next))

    followers.sort()

    for f in followers:
        cnt = dp_cnt[f[1]]
        if cnt <= skip:
            skip -= cnt
        else:
            reconstruct(f[1], skip, result)
            break

def klis(n, k, S):
    global dp_len, dp_cnt
    S += [-float('inf')]
    dp_len = make_length(n,S)
    dp_cnt = make_count(n,S)
    optsol = []
    reconstruct(-1,k-1,optsol)
    print(dp_len[-1] - 1)
    print(*optsol[1:])

# 테스트 케이스 입력
for _ in range(int(input())):
    n, k = map(int, input().split())
    S = list(map(int, input().split()))

    klis(n, k, S)
