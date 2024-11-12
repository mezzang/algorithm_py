def traversal(preorder, inorder):
    assert(len(preorder) == len(inorder))
    if preorder:
        root = preorder[0]
        pos = inorder.index(root)
        traversal(preorder[1:pos + 1], inorder[:pos])
        traversal(preorder[pos+1:], inorder[pos+1:])
        print(root, end = " ")

def inorder(preorder, postorder):
    assert(len(preorder) == len(postorder) and preorder[0] == postorder[-1])
    root = preorder[0]
    if len(preorder) == 1:
        print(root, end = " ")
    elif preorder:
        pos = postorder.index(preorder[1]) + 1
        inorder(preorder[1:pos + 1], postorder[:pos])
        print(root, end = " ")
        inorder(preorder[pos+1:], postorder[pos: -1])

for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    traversal(preorder, inorder)
    print()
    