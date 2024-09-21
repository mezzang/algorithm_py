# 중앙을 포함하는 직사각형 중 가증 큰 것을 찾기
def largest_in_between(h, left, mid, right):
    low, high = mid, mid + 1 #중앙 부분의 height 비교
    height = min(h[low], h[high]) #처음 직사각형의 높이를 작은 값 으로 설정(당연)
    ret = height * 2 #height는 넓이가 된다. 초기 직사각형의 넓이는 2칸이므로 *2
    while left < low or right > high: #low를 왼쪽으로 확장 또는 high를 오른쪽으로 확장 (확장해가면서 반복)
        # high가 right보다 작고 왼쪽으로 확장하는 것이 불가능하거나 오른쪽 확장이 유리할 때
        if high < right and (low == left or h[low - 1] < h[high + 1]):
            high += 1 #오른쪽으로 한 칸 확장
            height = min(height, h[high])
        else: 
            low -= 1 #그렇지 않으면 왼쪽으로 확장
            height = min(height, h[low])
        ret = max(ret, height * (high - low + 1)) #매번 ret을 비교하여 ret업데이트
    return ret

# 분할 정복 알고리즘. 히스토그램을 왼쪽과 오른쪽으로 나눠 재귀적으로 최대 직사각형을 구한다.
def fence(h, left, right):
    # 기저 사례: 판자가 하나만 남았을 때
    if left == right:
        return h[left]
    # 중앙을 포함하는 직사각형(largest_in_between)과 양쪽 부분 각각의 최대 직사각형 중에서 더 큰 직사각형을 반환한다.
    else:
        mid = (left + right) // 2
        # 왼쪽과 오른쪽의 최대 직사각형 넓이 계산
        ret = max(fence(h, left, mid), fence(h, mid + 1, right))
        # 두 부분에 모두 걸치는 경우의 가장 큰 사각형 고려
        return max(ret, largest_in_between(h, left, mid, right))
    

# 울타리 잘라내기 (메인코드)
for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    print(fence(h,0,n - 1))



