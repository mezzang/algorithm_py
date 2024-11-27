def make_graph(word):
    adj = [[0] *26 for _ in range(26)]
    for i in range(n-1):
        for x, y in zip(word[i], word[i + 1]):
            if x != y:
                adj[ord(x) - ord('a')][ord(y) - ord('a')] = 1
                break
    return adj

def dfs(here, adj, seen, order):
    seen[here] = True
    for there in range(26):
        if not seen[there] and adj[here][there]:
            dfs(there,adj, seen, order)
    order.append(here)

def topological_sort(adj):
    seen = [False] * 26
    order = []
    for i in range(26):
        if not seen[i]:
            dfs(i, adj, seen, order)
    order.reverse()

    for i in range(26):
        for j in range(i+1, 26):
            if adj[order[j]][order[i]]:
                return None
    return order

for _ in range(int(input())):
    n = int(input())
    word = [input() for _ in range(n)]
    adj = make_graph(word)
    order = topological_sort(adj)
    if not order:
        print("INVALID HYPOTHESIS")
    else:
        print("".join([chr(i + ord('a')) for i in order]))