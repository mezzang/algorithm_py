from itertools import product

#게임판 덮기 문제를 완전 탐색으로 해결
def boardcover(H, W, board):
    
    #편의를 위해 board의 값을 0(.)과 1(#)로 바꾼다.
    board2 = [[0] * W for _ in range(H)]  #모두 0으로 초기화
    for i, j in product(range(H), range(W)):
        board2[i][j] = [0,1][board[i][j] =='#']
    if sum([row.count(0) for row in board2]) % 3 !=0: #row.count(0) : 리스트 row에서 값이 0인 요소의 개수를 세는 파이썬 구문 count는 리스트의 메서드
        return 0
    else:
        return cover(board2, H, W)

#아직 채우지 못한 칸 중 가장 윗줄 가장 왼쪽에 있는 칸을 찾는다.
def find_white(board, H, W):
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                return i, j
    return -1, -1  #모든 칸을 확인했는데도 흰칸이 없으면 (-1,-1) 반환

coverType = [  #각 블록의 유형을 상대좌표의 목록으로 저장한다. 유형은 총 네 가지
    [(0,0),(1,0),(0,1)],
    [(0,0),(0,1),(1,1)],
    [(0,0),(1,0),(1,1)],
    [(0,0),(1,0),(1,-1)]
]

#board[i][j] == 1 : 덮인 칸(검은 칸)
#board[i][j] == 0 : 빈 칸(흰 칸)
def cover(board, H, W):
    y,x = find_white(board,H,W)
    if y == -1:
        return 1 #모든 칸을 채웠으므로 1을 반환한다.
    else:
        ret = 0
        for type in range(4):  #모든 블록 유형에 대해서 덮어본다.
            if(place(board,y,x,type,1,H,W)):  #delta가 1
                ret += cover(board,H,W)  #덮을 수 있으면 재귀호출 한다.
            place(board, y, x,type,-1,H,W)  #delta가 -1 덮은 블록을 제거한다.
        return ret
    

def place(board, y, x, type, delta, H, W):
    ok = True
    for i in range(3):
        ny = y + coverType[type][i][0] #y값이 변한다. y축에서 이동할 값 ny는 현재 위치 y에서 coverType에 정의된 y축 방향으로 이동한 새로운 좌표 y를 계산한다. 즉 ny는 y에서 dy 만큼 이동한 값
        nx = x + coverType[type][i][1] # x축에서 이동할 값
        if not ((0 <= ny < H) and (0 <= nx <W)):  #보드 밖으로 나간 경우
            ok = False
        else:
            board[ny][nx] += delta #delta가 1이면 덮고 -1이면 덮었던 블록을 제거한다. 
            if (board[ny][nx] > 1):
                ok = False
    return ok


    
#게임판 덮기 (실행 함수)
for _ in range(int(input())):  # _ : 특별한 변수의 값을 사용하지 않겠다.
    H, W = map(int, input().split())
    board = [input() for _ in range(H)]  #H번을 반복하며 각 줄(input())을 리스트에 저장한다.
    print(boardcover(H, W, board))  #흰 칸을 덮는 방법의 수