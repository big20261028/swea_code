import sys
sys.stdin = open('sample_input.txt','r')

from heapq import heappop, heappush

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    hq = []
    result = []
    for _ in range(N):
        order = input()
        if order[0] == '1':
            _, num = map(int,order.split())
            heappush(hq, -num)
        else:
            if hq:
                root = heappop(hq)
                result.append(-root)
            else:
                result.append(-1)

    print(f'#{tc} {" ".join(map(str, result))}')