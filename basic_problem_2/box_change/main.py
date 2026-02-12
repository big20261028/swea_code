import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1,T+1):
    n,q = map(int,input().split())
    orders = [ list(map(int,input().split())) for _ in range(q) ]

    boxs = [0] * n
    #print(orders)
    # i번째 작업일 때 i 값으로 박스의 값을 변경하는 문제

    for i,order in enumerate(orders):
        for idx in range(order[0]-1,order[1]):
            boxs[idx] = i+1
    print(f'#{tc} {" ".join(map(str,boxs))}')