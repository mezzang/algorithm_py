MOD = 1000000007
def fib4(n):
    if n <= 1:
        return n
    else:
        A = [[1,1], [1,0]]
        return mpow(A, n)[0][0]

def mpow(A, exp):
    result = [[1, 0], [0, 1]]  # 항등 행렬
    while exp > 0:
        if exp % 2 == 1:
            result = mmult(result, A)
        A = mmult(A, A)
        exp //= 2
    return result

def tiling(n):
    if n <= 2:
        return n
    else:
        if n <=2:
            return n
        else:
            A = [[1,1], [1,0]]
            return mpow(A, n)[0][0] 

def mmult(A, B):
    N, K, M = len(A), len(A[0]), len(B[0])
    C = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for k in range(K):
                C[i][j] = (C[i][j] + (A[i][k] * B[k][j])) % MOD
    return C

for _ in range(int(input())):
    n = int(input())
    print(tiling(n))
