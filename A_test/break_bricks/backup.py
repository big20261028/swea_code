import sys

sys.stdin = open('sample_input.txt', 'r')

from collections import deque
import copy

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def break_brick(deps, matrix):
    global min_val

    cnt = 0
    for row in matrix:
        cnt += W - row.count(0)

    if cnt == 0:
        min_val = 0
        return

    if deps == N:
        min_val = min(min_val, cnt)
        return

    for j in range(W):
        matrix2 = copy.deepcopy(matrix)
        for i in range(H):
            # 해당 좌표가 0이라면 continue
            if matrix2[i][j] == 0: continue

            # 해당 좌표값이 1이라면
            if matrix2[i][j] == 1:
                # 좌표값만 0으로 바꾸기
                matrix2[i][j] = 0

            # 좌표값이 1보다 크면
            else:
                # bfs로 탐색
                # 좌표값, 폭팔범위
                queue = deque()
                queue.append([(i, j), matrix2[i][j]])
                matrix2[i][j] = 0

                while queue:
                    (x, y), power = queue.popleft()
                    for dx, dy in dxy:
                        nx, ny = x, y
                        for d in range(power - 1):
                            nx += dx
                            ny += dy
                            if not (0 <= nx < H and 0 <= ny < W):
                                break
                            if matrix2[nx][ny] > 1:
                                queue.append([(nx, ny), matrix2[nx][ny]])
                            matrix2[nx][ny] = 0

                # 밑으로 밀착시키기
                # 세로열로 탐색하며 빈 리스트에 append
                # 0의 갯수만큼 곱한 값에 + 해서 다시 해당 열의 리스트 만들기
                # 그 리스트 데이터를 matrix2에 할당
                for y2 in range(W):
                    temp_list = []

                    for x2 in range(H):
                        if matrix2[x2][y2] != 0:
                            temp_list.append(matrix2[x2][y2])

                    zero_cnt = H - len(temp_list)
                    temp_list = [0] * zero_cnt + temp_list

                    for x2 in range(H):
                        matrix2[x2][y2] = temp_list[x2]

            # 처리된 matrix2 데이터와 deps 값 넘겨서 재귀
            break_brick(deps+1,matrix2)

            # 충돌한 블록 처리완료
            # 해당 라인은 이미 충돌 했으므로 다음 라인으로 넘어가기 위한 break
            break


T = int(input())
for tc in range(1, T + 1):
    # 구슬 쏠 횟수, 너비, 높이
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    min_val = float('inf')

    break_brick(0,matrix)

    print(f'#{tc} {min_val}')