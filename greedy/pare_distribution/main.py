import sys
sys.stdin = open('sin.txt','r')

T = int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    candies = list(map(int,input().split()))

    candies.sort(reverse=True)

    min_val = candies[0] - candies[n-1]

    for i in range(len(candies)-k+1):
        diff = candies[i] - candies[i+k-1]
        if diff < min_val:
            min_val = diff

    print(f'#{tc} {min_val}')
