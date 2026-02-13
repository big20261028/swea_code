import sys

sys.stdin = open('sample_input.txt' , 'r')

def is_in_range(x,y):
    if 0<=x<N and 0 <= y < N:
        return True
    return False

T = int(input())
for tc in range(1,T+1):
    # 세로, 가로, 배양시간
    N,M,K = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    #print(matrix)

    cells = []
    used_pos = []

    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                cell = {
                    'pos' : [i,j],
                    'power' : matrix[i][j],
                    'start' : matrix[i][j],
                    'end'   : matrix[i][j]+matrix[i][j],
                    'spawn' : 0
                }
                cells.append(cell)
                used_pos.append([i,j])

    # print(matrix[0])
    # print(matrix[1])
    dxy = [ (1,0),(-1,0),(0,-1),(0,1)]

    t = 0
    while t < K:
        for cell in cells[:]:
            if cell['start'] <= t < cell['end']:
                for dx,dy in dxy:
                    nx = cell['pos'][0] + dx
                    ny = cell['pos'][1] + dy
                    # 이미 사용중인 좌표라면
                    if [nx,ny] in used_pos:
                        for old_cell in cells[:]:
                            if old_cell['spawn'] == t and old_cell['pos'] == [nx,ny]:
                                if old_cell['power'] < cell['power']:
                                    old_cell['power'] = cell['power']
                                    old_cell['start'] = 1 + t + cell['power']
                                    old_cell['end'] = 1 + t + cell['power']*2


                    # 사용중인 좌표가 아니라면
                    else:
                        new_cell = {
                            'pos': [nx, ny],
                            'power': cell['power'],
                            'start': 1 + t + cell['power'],
                            'end': 1 + t + cell['power']*2 ,
                            'spawn': t
                        }
                        cells.append(new_cell)
                        used_pos.append([nx,ny])


        t += 1

    cnt = 0
    for cell in cells:
        if cell['spawn'] <= t < cell['end']:
            cnt += 1

    print(f'#{tc} {cnt}')