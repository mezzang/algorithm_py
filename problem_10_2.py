
def editorwars(n, m, reply):
    global parent, rank, enemy, size
    parent = list(range(n))
    rank = [1] * n
    enemy = [-1] * n
    size = [1] * n
    for i in range(m):
        c,a,b = reply[i]
        a, b = int(a), int(b)
        ret = ack(a, b) if c == "ACK" else dis(a, b)
        if not ret:
            return "CONTRADICTION AT " + str(i+1)
    return "MAX PARTY SIZE IS " + str(max_party())

def union(a,b):
    if a == -1 or b == -1:
        return max(a,b)
    p, q = find(a), find(b)
    if p != q:
        if rank[p] > rank[q]:
            p, q = q, p
        parent[p] = q
        if rank[p] == rank[q]:
            rank[q] += 1
        size[q] += size[p]
    return q

def find(a):
    if a == parent[a]:
        return a
    return find(parent[a])

def ack(a, b):
    p, q = find(a), find(b)
    if enemy[p] == q:
        return False
    a = union(p,q)
    b = union(enemy[p], enemy[q])
    enemy[a] = b
    if b != -1:
        enemy[b] = a
    return True

def dis(a, b):
    p, q = find(a), find(b)
    if p == q:
        return False
    a = union(p, enemy[q])
    b = union(q, enemy[p])
    enemy[a] = b
    enemy[b] = a
    return True

def max_party():
    ret = 0
    for i in range(n):
        if parent[i] == i and enemy[i] <= i:
            ret += max(size[i], size[enemy[i]])
    return ret

for _ in range(int(input())):
    n, m = map(int,input().split())
    reply = [input().split() for _ in range(m)]
    print(editorwars(n, m, reply))
