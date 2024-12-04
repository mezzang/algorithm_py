INF = float('inf')
from copy import deepcopy

def drunken(n, adj, delay):
    order = sorted([(delay[i], i) for i in range(n)])
    W = deepcopy(adj)
    for d, w in order :
        for i in range(n):
            for j in range(n):
                adj[i][j] = min(adj[i][j], adj[i][w] + adj[w][j])
                W[i][j] = min(W[i][j], adj[i][w] + adj[w][j] + d)
    return W

V, E = map(int, input().split())
delay = list(map(int, input().split()))
adj = [[INF] * V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a-1][b-1] = c
    adj[b-1][a-1] = c

for i in range(V): adj[i][i] = 0

W = drunken(V, adj, delay)
for _ in range(int(input())):
    s, t = map(int, input().split())
    print(W[s-1][t-1])
