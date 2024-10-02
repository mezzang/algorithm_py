from bisect import bisect_left

def lis(n,S):
    dp = [1]*n
    choices = [-1]*n
    for i in range(n-1,-1,-1):
        for j in range(i+1, n):
            if S[i] < S[j]:
                if dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
                    choices[i] = j
    return max(dp), choices


def reconstruct(start):
    global n,A,choices
    if start == -1:
        return[]
    else:
        return [A[start]] + reconstruct(choices[start])
    
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    optval, choices = lis(n,A)
    optsol = reconstruct(0)
    print(optval)
    print(*optsol)
    