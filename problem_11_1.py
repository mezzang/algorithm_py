import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self,n, arr):
        self.n = n
        self.arr = arr
        self.nodes = [0] * (4 * n)
        self.init(1,0,n-1)

    def init(self, node, left, right):
        if left == right:
            self.nodes[node] = self.arr[left]
            return self.nodes[node]
        else:
            mid = (left + right) // 2
            lmin = self.init(2*node, left, mid)
            rmin = self.init(2*node + 1, mid + 1, right)
            self.nodes[node] = min(lmin, rmin)
            return self.nodes[node]
    
    def query(self, node, low, high, left, right):
        if right < low or high < left:
            return float('inf')
        elif left <= low and high <= right:
            return self.nodes[node]
        else:
            mid = (low + high) // 2
            lmin = self.query(2*node, low, mid, left, right)
            rmin = self.query(2*node+1, mid + 1, high, left, right)
            return min(lmin, rmin)
def mordor(n, h, query):
    min_tree = SegmentTree(n, h)
    max_tree = SegmentTree(n, [-x for x in h])
    for a, b in query:
        range_min = min_tree.query(1,0,n-1,a,b)
        range_max = max_tree.query(1,0,n-1,a,b)
        print(-range_max - range_min)

for _ in range(int(input().strip())):
    n, q = map(int, input().split())
    h = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]
    mordor(n,h,query)