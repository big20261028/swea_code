import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    # n: 손님수, m:만들어지는 시간, k:만들어지는 개수
    n,m,k = map(int,input().split())
    customers = list(map(int, input().split()))

    customers.sort()

    sold = 0
    result = 'Possible'
    for t in customers:
        stock = ((t//m)*k) - sold
        if stock <= 0:
            result = "Impossible"
            break
        sold += 1

    print(f'#{tc} {result}')

