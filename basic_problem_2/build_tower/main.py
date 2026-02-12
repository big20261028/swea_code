import sys
sys.stdin = open('input5_sample.txt','r')

T = int(input())

from collections import deque

for tc in range(1,T+1):
    n,w1,w2 = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort(reverse=True)
    boxs = deque(arr)

    start = n - (w1+w2)
    end = n

    min_w = 0

    for i in range(start,end):
        if i < w1 and len(boxs) > 0:
            box = boxs.popleft()
            min_w += box * (i+1)
        if i < w2 and len(boxs) > 0:
            box = boxs.popleft()
            min_w += box * (i+1)

    print(f'#{tc} {min_w}')