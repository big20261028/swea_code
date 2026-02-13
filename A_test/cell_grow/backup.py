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
                                    old_cell['start'] = t + cell['power']
                                    old_cell['end'] = t + cell['power']*2


                    # 사용중인 좌표가 아니라면
                    else:
                        cell = {
                            'pos': [nx, ny],
                            'power': cell['power'],
                            'start': t + cell['power'],
                            'end': t + cell['power']*2,
                            'spawn': t
                        }
                        cells.append(cell)
                        used_pos.append([nx,ny])



        # for i in range(N):
        #     for j in range(M):
        #         target = matrix[i][j]
        #         if target == 0: continue
        #
        #         if target['비활성'] <= t < target['활성']:
        #             for dx,dy in dxy:
        #                 nx = i + dx
        #                 ny = j + dy
        #                 if is_in_range(nx,ny):
        #                     if matrix[nx][ny] == 0 or (matrix[nx][ny]['생성시간'] == t and matrix[nx][ny]['생명력'] < target['생명력'] ):
        #                         cell = {
        #                             '생명력': target['생명력'],
        #                             '비활성': t + target['생명력'],
        #                             '활성': t + (target['생명력']*2),
        #                             '생성시간': t
        #                         }
        #                         matrix[nx][ny] = cell


        t += 1

    cnt = 0
    for row in matrix:
        for cell in row:
            if cell == 0 : continue
            if cell['생성시간'] <= t < cell['활성']:
                cnt += 1

    print(f'#{tc} {cnt}')