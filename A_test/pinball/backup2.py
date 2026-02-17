import sys
sys.stdin = open('sample_input.txt','r')

def dfs(deps,x,y,st_pos,cnt,dr):
    global max_cnt

    if deps != 0:
        if (x,y) == st_pos or matrix[x][y] == -1:
            max_cnt = max(max_cnt,cnt)
            return

    dx,dy = dxy[dr_dict[dr]]
    nx,ny = x + dx, y + dy
    # 다음에 이동할 좌표가 외곽 벽인경우
    # block_dict[5]를 이용, 반사시킴
    if not (0 <= nx < N and 0 <= ny < N):
        cnt += 1
        dr = block_dict[5][dr]
        nx,ny = x,y
    # 이동할 좌표가 반사 가능한 블록인 경우
    elif 0 < matrix[nx][ny] <= 5:
        # 충돌 횟수를 1 추가
        cnt += 1
        # 다음에 이동할 방향을 전환
        dr = block_dict[matrix[nx][ny]][dr]
    # 이동할 좌표가 웜홀인 경우
    elif 6 <= matrix[nx][ny] <= 10:
        # 이동할 좌표 변경
        nx,ny = block_dict[matrix[nx][ny]][(nx,ny)]

    # 어느것도 해당되지 않을 경우, 그대로 진행
    x,y = nx,ny
    # 재귀 실시
    dfs(deps+1,x,y,st_pos,cnt,dr)

def count_knock(st_x,st_y,dr):

    x,y = st_x,st_y

    cnt = 0
    deps = 0
    while True:
        if deps != 0:
            if (x, y) == (st_x,st_y) or matrix[x][y] == -1:
                break

        dx, dy = dxy[dr_dict[dr]]
        nx, ny = x + dx, y + dy
        # 다음에 이동할 좌표가 외곽 벽인경우
        # block_dict[5]를 이용, 반사시킴
        if not (0 <= nx < N and 0 <= ny < N):
            cnt += 1
            dr = block_dict[5][dr]
            nx, ny = x, y
            # 만약 시작점이 블록이라면 블록으로 반사
            if 0 < matrix[nx][ny] <= 5:
                # 충돌 횟수를 1 추가
                cnt += 1
                # 다음에 이동할 방향을 전환
                dr = block_dict[matrix[nx][ny]][dr]
        # 이동할 좌표가 반사 가능한 블록인 경우
        elif 0 < matrix[nx][ny] <= 5:
            # 충돌 횟수를 1 추가
            cnt += 1
            # 다음에 이동할 방향을 전환
            dr = block_dict[matrix[nx][ny]][dr]
        # 이동할 좌표가 웜홀인 경우
        elif 6 <= matrix[nx][ny] <= 10:
            # 이동할 좌표 변경
            nx, ny = block_dict[matrix[nx][ny]][(nx, ny)]

        # 어느것도 해당되지 않을 경우, 그대로 진행
        x, y = nx, ny
        deps += 1
    return cnt


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    # 각 블록 별 굴절각 등록
    # 이 블록을 마주한 공의 진행 방향 : 꺾여나갈 방향
    # 진입방향 : 출력방향
    block_dict = { # 서 동 북 남
        #0 : { 'W':'W','E':'E','N':'N','S':'S' },
        1 : { 'W':'N','E':'W','N':'S','S':'E' },
        2:  { 'W':'S','E':'W','N':'E','S':'N' },
        3:  { 'W':'E','E':'S','N':'W','S':'N' },
        4:  { 'W':'E','E':'N','N':'S','S':'W' },
        5:  { 'W':'E','E':'W','N':'S','S':'N' },
        #-1: { 'W':'W','E':'E','N':'N','S':'S' },
    }

    # 웜홀 좌표 찾기
    temp_dict = {}
    for i in range(N):
        for j in range(N):
            pos_val = matrix[i][j]
            if pos_val < 6: continue
            if pos_val in temp_dict:
                block_dict[pos_val] = {
                    temp_dict[pos_val] : (i,j),
                    (i,j) : temp_dict[pos_val],
                }
            else:
                temp_dict[pos_val] = (i,j)

    #print(block_dict)

    dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]
    dxy_dr = [ 'N','S','E','W' ]
    dr_dict = {
        'W' : 3, 3 : 'W',
        'E' : 2, 2 : 'E',
        'S' : 0, 0 : 'S',
        'N' : 1, 1 : 'N',
    }
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0: continue
            for d in dxy_dr:
                #dfs(0, i, j, (i,j), 0, d)
                max_cnt = max(max_cnt,count_knock(i,j,d))

    print(f'#{tc} {max_cnt}')