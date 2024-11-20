import sys
input = sys.stdin.readline
TREE_SIZE = 1000000

class FenwickTree:
    def __init__(self, n):
        self.n = self.tree = [0] * (n+1)
    
    def add(self, pos, x):
        pos += 1
        while pos < len(self.tree):
            self.tree[pos] += x
            pos += (pos& -pos)
    
    def sum(self, pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += self.tree[pos]
            pos &= (pos - 1)
        return ret
    
def measuretime(n, A):
    tree = FenwickTree(TREE_SIZE)
    ret = 0
    for i in range(n):
        ret += tree.sum(TREE_SIZE - 1) - tree.sum(A[i])
        tree.add(A[i], 1)
    return ret

for _ in range(int(input().strip())):
    n = int(input().strip())
    A = list(map(int, input().split()))
    print(measuretime(n, A))
