import math
def lan(n, W):
    dist = [W[0][i] for i in range(n)]
    ret = 0
    for _ in range(n-1):
        min_dist = float('inf')
        for u in range(1,n):
            if 0 <= dist[u] < min_dist:
                min_dist = dist[u]
                vnear = u

        ret += math.sqrt(dist[vnear])
        dist[vnear] = -1

        for u in range(1,n):
            if dist[u] > W[u][vnear]:
                dist[u] = W[u][vnear]
    return ret


for _ in range(int(input())):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    W = [[0] * n for _ in range(n)]

    for u in range(n):
        for v in range(u, n):
            W[u][v] = W[v][u] = (x[u] - x[v])**2 + (y[u] - y[v])**2

    for _ in range(m):
        u,v = map(int,input().split())
        W[u][v] = W[v][u] = 0
    print(f"{lan(n,W):08f}")
