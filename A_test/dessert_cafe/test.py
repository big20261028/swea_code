import sys
sys.stdin = open('sample_input.txt','r')

# sys.stdin = open('sample_input.txt', 'r') # 제출 시 주석 처리

def dfs(x, y, path, dir):
    global max_val

    # 현재 방향으로 이동할 좌표
    nx = x + dxy[dir][0]
    ny = y + dxy[dir][1]

    # 1. 출발점으로 돌아왔는지 확인 (종료 조건)
    # 시작점과 같고, 적어도 사각형을 이루려면 경로 길이가 4 이상이어야 함
    if nx == start_pos[0] and ny == start_pos[1] and len(path) >= 4:
        max_val = max(max_val, len(path))
        return

    # 2. 범위 체크 및 방문 체크
    # 범위를 벗어나거나, 이미 먹은 디저트라면 진입 불가
    if not (0 <= nx < N and 0 <= ny < N) or matrix[nx][ny] in path:
        return

    # 3. 다음 칸으로 이동 (백트래킹)
    # 3-1. 직진하는 경우
    path.append(matrix[nx][ny])
    dfs(nx, ny, path, dir)

    # 3-2. 방향을 꺾는 경우 (현재 방향이 마지막 방향인 3이 아닐 때만)
    if dir < 3:
        dfs(nx, ny, path, dir + 1)

    # 복구
    path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 방향: 우하 -> 좌하 -> 좌상 -> 우상 (시계방향 마름모)
    # 이 순서대로 돌면 사각형을 그리며 원점으로 돌아오기 편합니다.
    dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    max_val = -1

    # 모든 점을 출발점으로 시도
    # 가지치기: 양옆, 아래로 최소한의 공간이 있어야 사각형 가능
    for x in range(N - 2):
        for y in range(1, N - 1):
            start_pos = (x, y)
            # 시작점 넣고 출발 (방향 인덱스 0)
            # path를 set()이 아닌 list로 쓰는 이유는 순서대로 넣고 빼기 위함 (속도는 set이 빠르지만 N이 작아 list도 무방)
            dfs(x, y, [matrix[x][y]], 0)

    print(f'#{tc} {max_val}')