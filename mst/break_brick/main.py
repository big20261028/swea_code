import sys
sys.stdin = open('sample_input.txt','r')

from copy import deepcopy

dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]

def find_top(target_y,matrix):
    for x in range(H):
        if matrix[x][target_y]:
            return x
    return -1

def brick_crash(tx, ty, matrix):
    stack = [((tx,ty),matrix[tx][ty])]
    matrix[tx][ty] = 0
    # visited = [ [False] * W for _ in range(H) ]
    # visited[tx][ty] = True

    while stack:
        (x, y), power = stack.pop()

        for dx,dy in dxy:
            nx,ny = x, y
            for d in range(power-1):
                nx += dx
                ny += dy
                if not (0 <= nx < H and 0 <= ny < W):
                    break
                # if visited[nx][ny]:
                #     continue
                if matrix[nx][ny] > 1:
                    stack.append(((nx,ny), matrix[nx][ny]))
                matrix[nx][ny] = 0

    return matrix

def matrix_sort(matrix):

    for j in range(W):
        temp_list = []
        for i in range(H):
            if matrix[i][j] != 0:
                temp_list.append(matrix[i][j])

        zero_cnt = H - len(temp_list)
        temp_list = ( [0] * zero_cnt ) + temp_list

        for i in range(H):
            matrix[i][j] = temp_list[i]

def do_break(deps,matrix):
    global min_val

    remain_cnt = W * H
    for row in matrix:
        remain_cnt -= row.count(0)

    if deps == N or remain_cnt == 0:
        min_val = min(min_val,remain_cnt)
        return

    for j in range(W):
        i = find_top(j,matrix)
        if i == -1: continue
        result_mtr = brick_crash(i, j, deepcopy(matrix))
        matrix_sort(result_mtr)
        do_break(deps + 1, result_mtr)


T = int(input())
for tc in range(1,T+1):
    # 구슬 발사 횟수, 가로, 세로
    N, W, H = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(H)]

    min_val = float('inf')
    do_break(0, deepcopy(matrix))

    print(f'#{tc} {min_val}')
