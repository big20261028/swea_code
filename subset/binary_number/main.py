import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    # binary = bin(M)
    # print(binary)
    stack = []
    #print(M)
    if M == 0: stack.append('0')
    while M>0:
        stack.append(str(M%2))
        M //= 2
    # 거꾸로된 이진수
    binary = ''.join(stack)
    #print(binary)
    flag = 'ON'
    for i in range(N):
        if i >= len(binary):
            flag = 'OFF'
            break
        if binary[i] == "0":
            flag = 'OFF'
            break
    print(f'#{tc} {flag}')