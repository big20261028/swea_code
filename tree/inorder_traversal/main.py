import sys
sys.stdin = open('input.txt', 'r')

class TreeNode:
    def __init__(self,root):
        self.val = root
        self.left = None
        self.right = None

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)

for tc in range(1, 11):
    N = int(input())
    node_list = [ TreeNode(i) for i in range(N+1) ]
    for i in range(N):
        data = input().split()
        l_c, r_c = None, None
        if len(data) == 2:
            num, val = data
        elif len(data) == 3:
            num, val, l_c = data
        else:
            num, val, l_c, r_c = data

        node = node_list[int(num)]
        node.val = val
        if l_c:
            node.left = node_list[int(l_c)]
        if r_c:
            node.right = node_list[int(r_c)]

    result = []
    inorder(node_list[1], result)

    print(f'#{tc} {"".join(result)}')
