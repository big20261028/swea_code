import sys
sys.stdin = open('input.txt','r')

# 가장 낮은, 가장 큰 실력의 차이가 K 이하인 팀
# 가장 많은 인원

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()
    max_val = 0

    for i in range(N):
        target = arr[i]
        cnt = 0
        for idx in range(i,N):
            max_val = max(max_val, cnt)
            if arr[idx] > target+K:
                break
            else:
                cnt += 1
            max_val = max(max_val, cnt)


    print(f'#{tc} {max_val}')
