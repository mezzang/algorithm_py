from heapq import heappush, heappop, heapify

def strjoin(strlen):
    heapify(strlen)
    ret = 0
    while len(strlen)>1: # 하나로 합쳐질 때까지
        len1 = heappop(strlen)
        len2 = heappop(strlen)
        heappush(strlen, len1 + len2)
        ret += len1 + len2
    return ret 

for _ in range(int(input())):
    n = int(input())
    strlen = list(map(int, input().split()))
    print(strjoin(strlen))

