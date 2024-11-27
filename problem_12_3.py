from collections import deque
def sortgame(n, perm):
    target = "01234567"[:n]
    queue = deque([(0, perm)])
    visited = set(perm)

    while queue:
        dist, here = queue.popleft()
        if here == target: return dist
        for i in range(n-1):
            for j in range(i+2, n+1):
                there = here[:i] + here[i:j][::-1] + here[j:]
                if there not in visited:
                    queue.append((dist + 1, there))
                    visited.add(there)
    return -1

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    sort = sorted(nums)
    perm = [sort.index(x) for x in nums]
    print(sortgame(n, "".join(map(str, perm))))
