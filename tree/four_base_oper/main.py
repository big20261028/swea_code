import sys
sys.stdin = open('input.txt', 'r')

class TreeNode:
    def __init__(self,root):
        self.val = root
        self.left = None
        self.right = None

def do_cal(oper,a,b):
    a, b = int(a), int(b)
    if oper == '+':
        return a + b
    if oper == '-':
        return a - b
    if oper == '/':
        return int(a / b)
    if oper == '*':
        return a * b

def postorder(root,stack):
    if root:
        postorder(root.left, stack)
        postorder(root.right, stack)
        if root.val in ['+', '-', '*', '/']:
            n2 = stack.pop()
            n1 = stack.pop()
            result = do_cal(root.val,n1,n2)
            stack.append(result)
        else:
            stack.append(int(root.val))

T = 10
for tc in range(1,T+1):
    N = int(input())
    # 입력값 : 정점, 값, 왼 자식번호, 오른 자식번호
    node_list = [ TreeNode(i) for i in range(N+1) ]
    for _ in range(N):
        data = list(input().split())
        l_c, r_c = None, None
        if len(data) <= 2:
            num, val = data
        elif len(data) <= 3:
            num, val, l_c = data
        else:
            num, val, l_c, r_c = data
        node = node_list[int(num)]
        node.val = val
        if l_c:
            node.left = node_list[int(l_c)]
        if r_c:
            node.right = node_list[int(r_c)]

    #print(node_list)
    stack = []
    postorder(node_list[1],stack)
    print(f'#{tc} {stack[0]}')
