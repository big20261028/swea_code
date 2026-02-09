### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    orders = [ list(map(int, input().split())) for _ in range(m)]
    board = [ list(0 for _ in range(n)) for _ in range(n) ]

    # 0 : 빈칸, 1: 흑돌, 2: 백돌
    # 초기 설정
    board[(n//2)-1][(n//2)-1] = 2
    board[(n//2)-1][(n//2)] = 1
    board[(n//2)][(n//2)-1] = 1
    board[(n//2)][(n//2)] = 2

    dxy = [ (1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1) ]

    for x,y,c in orders:
        x -= 1
        y -= 1

        board[x][y] = c

        # for row in board:
        #     print(row)
        # print('=========')

        for dx,dy in dxy:
            nx, ny = x, y
            target = []
            while True:
                nx += dx
                ny += dy
                # 판의 크기에서 벗어난다면 => 무효, 타겟 리스트 비우기
                if not (0 <= nx < n and 0 <= ny < n):
                    target.clear()
                    break
                # 돌이 놓여져 있지 않다면 => 무효, 타겟 리스트 비우기
                elif board[nx][ny] == 0:
                    target.clear()
                    break
                # 돌의 색깔이 c와 같다면 => 멈추기, 타겟 리스트 유지
                elif board[nx][ny] == c:
                    break
                # 아무것도 해당되지 않으면( 색깔이 c와 다르면 ) => 타겟 리스트에 추가
                else:
                    target.append((nx,ny))
            for i,j in target:
                board[i][j] = c

    w_stone = 0
    b_stone = 0
    for row in board:
        for stone in row:
            if stone == 1:
                w_stone += 1
            elif stone == 2:
                b_stone += 1

    #result = (w_stone,b_stone)
    print(f"#{test_case} {w_stone} {b_stone}")
