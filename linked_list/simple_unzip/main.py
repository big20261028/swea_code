import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [ list(input().split()) for _ in range(n) ]

    stack = []

    print(f'#{test_case}')

    for char, num in arr:
        for i in range(int(num)):
            stack.append(char)
            if len(stack) == 10:
                print(''.join(stack))
                stack.clear()

    if len(stack) > 0:
        print(''.join(stack))
