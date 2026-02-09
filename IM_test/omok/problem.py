### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
def find_omok(n,matrix,dxy):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'o':
                for dx,dy in dxy:
                    nx,ny = i,j
                    cnt = 1
                    while True:
                        nx += dx
                        ny += dy
                        if 0<=nx<n and 0<=ny<n and matrix[nx][ny]=='o':
                            cnt += 1
                        else:
                            break
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [ list(input()) for _ in range(n) ]

    dxy = [ (1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1) ]

    flag = find_omok(n,matrix,dxy)

    result = flag
    print(f"#{test_case} {result}")
