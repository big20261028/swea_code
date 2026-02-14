import sys

sys.stdin = open('sample_input.txt', 'r')


def is_in_range(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def find_max_dessert(deps, pos, total, move_cnt, direction=-1):
    global max_val
    if deps == 4:
        if move_cnt[0] == move_cnt[2] and move_cnt[1] == move_cnt[3]:
            max_val = max(max_val, sum(total))
        return

    if direction == -1:
        # 방향
        for i in range(4):
            # 거리
            last_m = 0
            for m in range(1, N - 1):
                last_m = m
                nx = pos[0] + dxy[i][0] * m
                ny = pos[1] + dxy[i][1] * m
                if not (is_in_range(nx, ny) and visited[nx][ny] and matrix[nx][ny] not in total):
                    break
                visited[nx][ny] = False
                total.append(matrix[nx][ny])
                move_cnt[i] += 1
                find_max_dessert(deps + 1, (nx, ny), total, move_cnt, i)

            # 리스트 초기화 해주기
            for m2 in range(1, last_m):
                nx2 = pos[0] + dxy[i][0] * m2
                ny2 = pos[1] + dxy[i][1] * m2
                visited[nx2][ny2] = True
                total.pop()
                move_cnt[i] -= 1

    else:
        # 방향
        dr = (direction + 1) % 4
        last_m = 0
        distance = N - 1
        # 반대쪽 방향 이동을 한 상태라면
        if move_cnt[(dr + 2) % 4] != 0: distance = move_cnt[(dr + 2) % 4] + 1
        # 거리
        for m3 in range(1, distance):
            last_m = m3
            nx3 = pos[0] + dxy[dr][0] * m3
            ny3 = pos[1] + dxy[dr][1] * m3
            if not (is_in_range(nx3, ny3) and visited[nx3][ny3] and matrix[nx3][ny3] not in total):
                break
            visited[nx3][ny3] = False
            total.append(matrix[nx3][ny3])
            move_cnt[dr] += 1
            find_max_dessert(deps + 1, (nx3, ny3), total, move_cnt, dr)

            # 리스트 초기화 해주기
        for m4 in range(1, last_m):
            nx4 = pos[0] + dxy[dr][0] * m4
            ny4 = pos[1] + dxy[dr][1] * m4
            visited[nx4][ny4] = True
            total.pop()
            move_cnt[dr] -= 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 순서 : 좌상, 우상, 우하, 좌하
    dxy = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

    max_val = 0
    move_cnt = [0, 0, 0, 0]
    total = []
    visited = [[True] * N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            start_pos = (x, y)
            # visited[x][y] = False
            total.append(matrix[x][y])
            find_max_dessert(0, (x, y), total, move_cnt)
            # visited[x][y] = True
            total.pop()

    if max_val == 0:
        max_val = -1

    print(f'#{tc} {max_val}')
