
def insertion(n, shifted):
    A = list(range(1, n+1))
    B = []

    for i in range(n-1, -1, -1):
        move = shifted[i]
        item = A[i-move]
        A.pop(i - move)
        B.append(item)
    return B[::-1]

for _ in range(int(input())):
    n = int(input())
    shifted = list(map(int, input().split()))
    print(*insertion(n, shifted))
