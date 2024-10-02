def packing(i, capacity):
    global n, w, p, cache
    if i == n or capacity <= 0:
        return 0
    elif cache[i][capacity] != -1:
        return cache[i][capacity]
    else:
        pick = 0
        if capacity >= w[i]:
            pick = packing(i+1, capacity -w[i]) + p[i]
        drop = packing(i+1, capacity)

        cache[i][capacity] = max(drop, pick)
        return cache[i][capacity]
    
def reconstruct(i, c):
    global n, items, w
    if i == n:
        return []
    elif packing(i, c) == packing(i+1,c):
        return reconstruct(i+1,c)
    else:
        return [items[i][0]] + reconstruct(i + 1, c - w[i])
    
for _ in range(int(input())):
    n, W = map(int,input().split())
    items = [input().split() for _ in range(n)]

    w = [int(items[i][1]) for i in range(n)]
    p = [int(items[i][2]) for i in range(n)]

    cache = [[-1] * (W +1) for _ in range(n+1)]

    optival = packing(0,W)

    optsol = reconstruct(0,W)

    print(optival, len(optsol))
    print(*optsol, sep='\n')

