import sys
sys.stdin = open('input.txt','r')

T = int(input())

nums = [ 2, 3, 5, 7, 11 ]

for tc in range(1,T+1):
    target = int(input())
    cnt  = [ 0, 0, 0, 0, 0  ]

    while target > 1:
        # print(target)
        # print(cnt)
        for idx,num in enumerate(nums):
            if target%num == 0:
                target = target//num
                cnt[idx] += 1
                break
    print(f'#{tc} {" ".join(map(str,cnt))}')
