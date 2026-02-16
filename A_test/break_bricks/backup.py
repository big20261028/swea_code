import sys

sys.stdin = open('sample_input.txt', 'r')

from collections import deque
import copy

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def break_brick(deps, matrix):
    global max_val

    if deps == N:
        cnt = 0
        for row in matrix:
            cnt += N - row.count(0)
        max_val = max(max_val, cnt)

    for j in range(W):
        matrix = copy.deepcopy(matrix)
        for i in range(H):
            # 해당 좌표가 0이라면 continue
            if matrix[i][j] == 0: continue

            # 해당 좌표값이 1이라면
            if matrix[i][j] == 1:
                # 좌표값만 0으로 바꾸기
                matrix[i][j] = 0

            # 좌표값이 1보다 크면
            else:
                # bfs로 탐색
                # 좌표값, 폭팔범위
                queue = deque()
                queue.append([(i, j), matrix[i][j]])

                while queue:
                    (x, y), power = queue.popleft()
                    for dx, dy in dxy:
                        nx, ny = x, y
                        for d in range(power - 1):
                            nx += dx
                            ny += dy
                            if not (0 <= nx < H and 0 <= ny < W):
                                break
                            if matrix[nx][ny] > 1:
                                queue.append([(nx, ny), matrix[nx][ny]])
                            matrix[nx][ny] = 0

            # 밑으로 밀착시키기
            # 세로열로 탐색하며 빈 리스트에 append
            # 0의 갯수만큼 곱한 값에 + 해서 다시 해당 열의 리스트 만들기
            # 그 리스트 데이터를 matrix에 할당

            # 충돌한 블록 처리완료
            break


T = int(input())
for tc in range(1, T + 1):
    # 구슬 쏠 횟수, 너비, 높이
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    max_val = 0

