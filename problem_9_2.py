import bisect
MOD = 20090711

class RNG:
    def __init__(self, a, b):
        self.seed = 1983
        self.a = a
        self.b = b
    
    def next(self):
        ret = self.seed
        self.seed = ((self.seed * self.a) % MOD + self.b) % MOD
        return ret

def runningmedian(n, rng):
    num = []
    ret = 0
    for k in range(1, n+1):
        next = rng.next()
        bisect.insort(num, next)
        ret = (ret + num[(k-1)//2]) % MOD
    return ret

for _ in range(int(input())):
    n,a,b = map(int, input().split())
    rng = RNG(a, b)
    print(runningmedian(n, rng))