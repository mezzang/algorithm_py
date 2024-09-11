linked = {
    0:[0,1,2],
    1:[3,7,9,11],
    2:[4,10,14,15],
    3:[0,4,5,6,7],
    4:[6,7,8,10,12],
    5:[0,2,14,15],
    6:[3,14,15],
    7:[4,5,7,14,15],
    8:[1,2,3,4,5],
    9:[3,4,5,9,13]
}

D = {i:[] for i in range(16)}
for i in range(10):
    for j in linked[i]:
        D[j].append(i)
    
        
sequence = [
(8, linked[4]), # 8 번 시계 , 4 번 스위치
(11 , linked[1]), # 11 번 시계 , 1 번 스위치
(13 , linked[9]), # 13 번 시계 , 9 번 스위치
(6 , linked[3]), # 6 번 시계 , 3 번 스위치
(10, linked[2]), # 10 번 시계 , 2 번 스위치
(7, linked[7]), # 7 번 시계 , 7 번 스위치
(4 , linked[8]), # 4 번 시계 , 8 번 스위치
(1 , linked[0]), # 1 번 시계 , 0 번 스위치
(3 , linked[6]), # 3 번 시계 , 6 번 스위치
(0 , linked[5]), # 0 번 시계 , 5 번 스위치
]




def clocksync(clocks):
    ret = 0
    for clock, linked_clock in sequence:
        cnt = (4-clocks[clock]) % 4
        for other in linked_clock:
            clocks[other] = (clocks[other] + cnt) % 4
        ret += cnt
    return -1 if any(clocks) else ret
            
            
INF = 31

for _ in range(int(input())):
    clocks = [(int(x)//3) % 4 for x in input().split()]
    mincnt = clocksync(clocks)
    print(mincnt if mincnt < INF else -1)
