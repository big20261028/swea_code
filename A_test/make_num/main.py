import sys
sys.stdin = open('sample_input.txt','r')

'''
연산자 객체를 순회?

'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    operates = list(map(int,input().split()))
    numbers = list(map(int,input().split()))

    oper = ['+','-','*','/']
    op_st = ''
    for i in range(4):
        op_st += oper[i] * operates[i]

    #print(op_st)








