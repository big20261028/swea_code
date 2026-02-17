import sys
sys.stdin = open('sample_input.txt','r')

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def count_knock(st_x,st_y,dr):
    x,y = st_x,st_y
    cnt = 0

    while True:
        dx, dy = dxy[dr]
        nx, ny = x + dx, y + dy

        if (nx, ny) == (st_x, st_y):
            break

        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == -1:
            break

        if not (0 <= nx < N and 0 <= ny < N):
            cnt += 1
            dr = block_dict[5][dr]
            x, y = nx, ny
            continue

        elif 1 <= matrix[nx][ny] <= 5:
            cnt += 1
            dr = block_dict[matrix[nx][ny]][dr]  # 방향 굴절
            x, y = nx, ny  # 블록 위로 이동 인정
            continue

        elif 6 <= matrix[nx][ny] <= 10:
            # 웜홀 반대편으로 점프
            nx, ny = block_dict[matrix[nx][ny]][(nx, ny)]
            x, y = nx, ny

        else:
            x, y = nx, ny

    return cnt

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    # 각 블록 별 굴절각 등록
    # 이 블록을 마주한 공의 진행 방향 : 꺾여나갈 방향
    # 진입방향 : 출력방향
    block_dict = {
        1: {0: 2, 1: 0, 2: 3, 3: 1},
        2: {0: 1, 1: 2, 2: 3, 3: 0},
        3: {0: 1, 1: 3, 2: 0, 3: 2},
        4: {0: 3, 1: 0, 2: 1, 3: 2},
        5: {0: 1, 1: 0, 2: 3, 3: 2},
    }

    # 웜홀 좌표 찾기
    temp_dict = {}
    for i in range(N):
        for j in range(N):
            pos_val = matrix[i][j]
            if pos_val < 6: continue
            if pos_val in temp_dict:
                p1 = temp_dict[pos_val]
                p2 = (i, j)
                block_dict[pos_val] = {p1: p2, p2: p1}
            else:
                temp_dict[pos_val] = (i, j)

    max_cnt = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0: continue
            for d in range(4):
                max_cnt = max(max_cnt, count_knock(i, j, d))

    print(f'#{tc} {max_cnt}')