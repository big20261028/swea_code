### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(n)]

    dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]

    # 가장 높은 지점 찾기
    max_h = 0
    start_pos = []
    for i,row in enumerate(matrix):
        for j,h in enumerate(row):
            if h > max_h:
                start_pos.clear()
                max_h = h
                start_pos.append((i,j))
            elif h == max_h:
                start_pos.append((i,j))
    #print(start_pos)

    max_cnt = 0

    # 델타탐색 시작
    for x,y in start_pos:
        cnt = 0
        while True:
            cnt += 1
            min_h = matrix[x][y]
            min_pos = [0,0]
            for dx,dy in dxy:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if matrix[nx][ny] < min_h:
                        min_h = matrix[nx][ny]
                        min_pos = [nx,ny]
            if min_h == matrix[x][y]:
                break
            x,y = min_pos
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{test_case} {max_cnt}')
