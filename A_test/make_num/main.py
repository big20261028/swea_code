import sys
sys.stdin = open('sample_input.txt','r')

'''
부분조합, 백트래킹을 해야하는 문제
다시 풀어보기
'''

from collections import deque

def generate_subset(deps):
    global min_val, max_val

    if deps == N-1:
        min_val = min(min_val,numbers[0])
        max_val = max(max_val,numbers[0])
        return

    for i in range(4):
        if operates[i] == 0: continue
        operates[i] -= 1
        op = oper[i]
        n1 = numbers.popleft()
        n2 = numbers.popleft()
        if op == '+':
            numbers.appendleft(n1 + n2)
        elif op == '-':
            numbers.appendleft(n1 - n2)
        elif op == '*':
            numbers.appendleft(n1 * n2)
        elif op == '/':
            numbers.appendleft(int(n1 / n2))
        generate_subset(deps+1)
        #백트래킹
        operates[i] += 1
        numbers.popleft()
        numbers.appendleft(n2)
        numbers.appendleft(n1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    operates = list(map(int,input().split()))
    numbers = deque(list(map(int,input().split())))

    oper = ['+','-','*','/']
    max_val = float('-inf')
    min_val = float('inf')
    generate_subset(0)
    print(f'#{tc} {max_val-min_val}')








