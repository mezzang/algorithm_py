for _ in range(int(input().strip())):
    n, W = map(int, input().split())
    items = [input().split() for _ in fange(n)]

    items.sort(key = lambda x: int(x[2]) / int(x[1]), reverse = True)
    W = [int(items[i][1]) for i in range(n)]
    p = [int(items[i][2]) for i in range(n)]
    optval, optsol = packing(n,W,w,p)
    print(optval, len(optsol))
    print(*optsol, sep = '\n')

def packing(n, W, w, p):
    global items, maxprofit, include
    maxprofit = [False] * n
    search(-1,0,0)
    return maxprofit, [items[i][0] for i in range(n) if best[i]]