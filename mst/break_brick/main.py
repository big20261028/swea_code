import sys
sys.stdin = open('sample_input.txt','r')

dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]

def find_top(target_y):
    for x in range(H):
        if matrix[x][target_y]:
            return x
    return -1

def brick_crash(tx, ty):
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
                if not (0 <= nx < H and 0 <= ny < H):
                    break
                # if visited[nx][ny]:
                #     continue
                if matrix[nx][ny] > 1:
                    stack.append(((nx,ny), matrix[nx][ny]))
                matrix[nx][ny] = 0

def matrix_sort(matrix):
    pass




T = int(input())
for tc in range(1,T+1):
    # 구슬 발사 횟수, 가로, 세로
    N, W, H = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(H)]

