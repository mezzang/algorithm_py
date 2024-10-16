from bisect import bisect_left
# 출전 순서 정하기 문제 탐욕적 알고리즘
def matchorder(n, russian, korean):
    korean.sort()
    wins = 0
    for i in range(n):
        if korean[-1] < russian [i]: #korean[-1]은 레이팅 가장 높은 선수
            korean.pop(0)
        else:
            wins += 1
            korean.pop(bisect_left(korean, russian[i]))
    return wins




# 구현
for _ in range(int(input())):
    n = int(input())
    russian = list(map(int, input().split()))
    korean = list(map(int, input().split()))
    print(matchorder(n, russian, korean))
