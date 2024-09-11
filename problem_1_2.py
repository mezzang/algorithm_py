import sys
input = sys.stdin.readline
INF = float('inf')

def maxsum_crossing(low, mid, high):
    left = -INF; curs = 0
    for i in range(mid, low -1, -1):
        curs += A[i]
        left = max(left, curs)
    
    right = -INF; curs = 0
    for j in range(mid + 1, high + 1):
        curs += A[j]
        right = max(right, curs)
    
    
    return left + right

def maxsum(low, high):
    if low == high:
        return max(A[low], 0)
    else:
        mid = (low + high) // 2
        lmax = maxsum(low, mid)
        rmax = maxsum(mid + 1, high)
        cmax = maxsum_crossing(low, mid, high)
        return max(lmax, rmax, cmax)

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    print(maxsum(0, N-1))