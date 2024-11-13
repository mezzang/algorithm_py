INF = float('inf')

def tpath():
    global adj, weights
    adj = [{} for _ in range(n)]
    for a,b,w in edges:
        adj[a][b] = adj[b][a] = w
    weights = {edges[i][2] for i in range(m)}
    weights = sorted(list(weights))
    return min_diff()

def min_diff():
    ret = INF
    for lo in range(len(weights)):
        for hi in range(lo+1, len(weights)):
            if has_path(weights[lo], weights[hi]):
                ret = min(ret, weights[hi] - weights[lo])
                break
    return ret

def has_path(lo, hi):
    global visited
    visited = [False] * n
    return dfs(0, lo, hi)

def dfs(here, lo, hi):
    if here == n - 1:
        return True
    else:
        visited[here] = True
        for there, weight in adj[here].items():
            if not visited[there] and (lo <= weight <= hi):
                if dfs(there, lo, hi):
                    return True
        return False
    
for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    ret = tpath()
    print(0 if ret == INF else ret)