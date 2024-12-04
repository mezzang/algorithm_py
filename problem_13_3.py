INF = float('inf')

def pathfind(n, D):
    for i in range(n):
        D[i][i] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = D[i][j] or (D[i][k] and D[k][j])


def timetrip(src, target, n, adj, reachable):
    upper = [INF] * n
    upper[src] = 0
    for _ in range(n-1):
        for here in range(n):
            for there, cost in adj[here]:
                upper[there] = min(upper[there], upper[here] + cost)
    
    for here in range(n):
        for there, cost in adj[here]:
            if upper[there] > upper[here] + cost:
                if reachable[src][here] and reachable[here][target]:
                    return - INF
    return upper[target]

for _ in range(int(input())):
    n, m = map(int, input().split())
    adj1 = [[] for _ in range(n)]
    adj2 = [[] for _ in range(n)]
    reachable = [[False] * n for _ in range(n)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        adj1[a].append((b,d))
        adj2[a].append((b, -d))
        reachable[a][b] = True

    pathfind(n, reachable)

    ret1 = timetrip(0,1,n, adj1, reachable)
    ret2 = timetrip(0,1,n,adj2, reachable)

    if not reachable[0][1]: print("UNREACHABLE")
    else: 
        print("INFINITY" if ret1 == -INF else ret1, end = " ")
        print("INFINITY" if ret2 == -INF else -ret2)