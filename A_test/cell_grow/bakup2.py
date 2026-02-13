import sys
sys.stdin = open('sample_input.txt' , 'r')

'''
1차시도 타임 아웃

'''

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

    # 세포를 관리하는 법
    # 좌표를 키/ 세포 정보를 벨류로 관리해보자
    cells = {}

    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                cell = {
                    'pos' : [i,j],
                    'power' : matrix[i][j],
                    'start' : matrix[i][j],
                    'end'   : matrix[i][j]+matrix[i][j],
                    'spawn' : 0,
                    'life': True
                }
                cells[(i,j)] = cell

    # print(matrix[0])
    # print(matrix[1])
    dxy = [ (1,0),(-1,0),(0,-1),(0,1)]

    t = 0
    while t < K:
        for pos,cell in cells.copy():
            # 죽은 세포면 패스
            if not cell['life']: continue

            if cell['start'] <= t < cell['end']:
                for dx, dy in dxy:
                    nx = cell['pos'][0] + dx
                    ny = cell['pos'][1] + dy
                    if (nx,ny) in cells:
                        target = cells[(nx,ny)]
                        if target['spawn'] == t and target['power'] < cell['power']:
                            target['power'] = cell['power']
                            target['start'] = 1 + t + cell['power']
                            target['end'] = 1 + t + cell['power']*2


                    else:
                        new_cell = {
                            'pos': [nx, ny],
                            'power': cell['power'],
                            'start': 1 + t + cell['power'],
                            'end': 1 + t + cell['power'] * 2,
                            'spawn': t,
                            'life': True
                        }
                        cells[(nx,ny)] = new_cell
            elif t >= cell['end']:
                cell['life'] = False

        t += 1

    cnt = 0
    for cell in cells:
        if cell['spawn'] <= t < cell['end']:
            cnt += 1

    print(f'#{tc} {cnt}')