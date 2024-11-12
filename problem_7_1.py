def search1(food, edible, chosen):
    global n, m, best, eaters
    if chosen >= best: return # 가지 치기
    if food == m:
        if all(edible): best = chosen
    else:
        #food를 만들지 않는 경우
        search1(food + 1, edible, chosen)
         # food를 만드는 경우
        for j in eaters[food]: edible[j] += 1
        search1(food + 1, edible, chosen + 1)
        for j in eaters[food]: edible[j] -= 1
        

for _ in range(int(input())):
    n, m = map(int, input().split())
    friends = {k:i for  i,k in enumerate(input().split())}
    eaters = {i:[friends[name] for name in input().split()[1:]] for i in range(m)}
    best = m + 1
    search1(0,[0]*n,0)
    print(best)


