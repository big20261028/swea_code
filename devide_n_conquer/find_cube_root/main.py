import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 이분탐색 실시
    top, bottom = 10 ** 6, 1
    result = -1
    while bottom <= top:
        middle = (top + bottom) // 2
        cube_val = middle ** 3
        if cube_val == N:
            result = middle
            break
        elif cube_val < N:
            bottom = middle + 1
        elif cube_val > N:
            top = middle - 1
    print(f'#{tc} {result}')
