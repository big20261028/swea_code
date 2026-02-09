### 제출 전에 지우기 ###
import sys
sys.stdin = open("in1.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
def kill_count(i,j,dxy,matrix):
    cnt = matrix[i][j]
    for dx, dy in dxy:
        nx, ny = i, j
        for area in range(m - 1):
            nx += dx
            ny += dy
            if 0 <= nx < n and 0 <= ny < n:
                cnt += matrix[nx][ny]
            else:
                break
    #         print(nx,ny)
    # print(cnt)
    return cnt

# 테스트 케이스
T = int(input())
#T = 1
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(n) ]

    dxy1 = [(1,0),(-1,0),(0,1),(0,-1)]
    dxy2 = [(1,1),(-1,1),(1,-1),(-1,-1)]

    max_kill = 0

    for i in range(n):
        for j in range(n):
            cnt1 = kill_count(i,j,dxy1,matrix)
            cnt2 = kill_count(i,j,dxy2,matrix)
            pos_max = max(cnt1,cnt2)
            if pos_max > max_kill:
                max_kill = pos_max
            #print(pos_max)
            # for dx,dy in dxy1:
            #     nx,ny = i,j
            #     for area in range(m-1):
            #         nx += dx
            #         ny += dy
            #         if 0 <= nx < n and 0 <= ny < n:
            #             cnt1 += matrix[nx][ny]
            #         else:
            #             break
            # if cnt1 > pos_max:
            #     pos_max = cnt1
            #
            # cnt2 = 0
            # for dx,dy in dxy2:
            #     nx,ny = i,j
            #     for area in range(m-1):
            #         nx += dx
            #         ny += dy
            #         if 0 <= nx < n and 0 <= ny < n:
            #             cnt2 += matrix[nx][ny]
            #         else:
            #             break
            # if cnt2 > pos_max:
            #     pos_max = cnt2
            #
            # if pos_max > max_kill:
            #     max_kill = pos_max

    result = max_kill
    print(f"#{test_case} {result}")
