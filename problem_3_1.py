#정적 변수를 이용하여 quadtree에서 한 문자씩 꺼내어 반환
def get_next(quadtree):
     get_next.idx += 1
     return quadtree[get_next.idx - 1]

#쿼드 트리를 뒤집어서 반환
def quadtree_reverse(quadtree):
     head = get_next(quadtree)
     if head in "bw":
          return head
     else:
        #   'x'인 경우 4분할을 재귀적으로 처리
          qt1 = quadtree_reverse(quadtree)
          qt2 = quadtree_reverse(quadtree)
          qt3 = quadtree_reverse(quadtree)
          qt4 = quadtree_reverse(quadtree)

          return "x" + qt3 + qt4 + qt1 + qt2
     
# 쿼드 트리 뒤집기
for i in range(int(input())):
     quadtree = input()
     get_next.idx = 0 #정적 변수로 인덱스를 초기화
     reversed = quadtree_reverse(quadtree)
     print(reversed)
