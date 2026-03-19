import sys
sys.stdin = open('input.txt', 'r')

dxy = [(1 ,0), (-1 ,0), (0 ,1), (0 ,-1)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    max_move_cnt = 0
    room_n = float('inf')

    for i in range(N):
        for j in range(N):
            # dfs 탐색
            stack = [[i,j, 1]]

            while stack:
                x, y, move = stack.pop()

                if move == max_move_cnt:
                    room_n = min(room_n, matrix[i][j])
                elif move > max_move_cnt:
                    max_move_cnt = move
                    room_n = matrix[i][j]

                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == matrix[x][y]+1:
                        stack.append([nx,ny,move + 1])


    print(f'#{tc} {room_n} {max_move_cnt}')


