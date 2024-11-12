def search2(edible, chosen):
    global n, m, best, eaters, eatables
    if chosen >= best: return
    try:
        first = edible.index(0)
    except:
        best = chosen
    else:
        for food in eatables[first]:
            for j in eaters[food]: edible[j] += 1
            search2(edible, chosen + 1)
            for j in eaters[food]: edible[j] -= 1

for _ in range(int(input())):
    n, m = map(int, input().split())
    friends = {k:i for i,k in enumerate(input().split())}
    eaters = {i:[friends[name] for name in input().split()[1:]] for i in range(m)}
    eatables = {i:[] for i in range(n)}
    for k in eaters:
        for v in eaters[k]:
            eatables[v].append(k)
    best = m + 1
    search2 ([0]*n, 0)
    print(best)

