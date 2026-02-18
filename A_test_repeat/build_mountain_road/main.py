import sys

sys.stdin = open('sample_input.txt','r')

dxy = [ (1,0),(-1,0),(0,1),(0,-1)]

def find_max_len(x,y,flag,len,visited):
    global max_len

    max_len = max(max_len,len)

    h = 1
    st_h = matrix[x][y]

    if flag:
        h += K

    for dx,dy in dxy:
        nx,ny = x+dx, y+dy
        if not (0 <= nx < N and 0 <= ny < N and visited[nx][ny]):
            continue
        end_h = matrix[nx][ny]
        for dig in range(h):
            if st_h > (end_h - dig):
                visited[nx][ny] = False
                if dig == 0:
                    find_max_len(nx,ny,flag,len+1,visited)
                else:
                    matrix[nx][ny] -= dig
                    find_max_len(nx, ny, False, len + 1, visited)
                    matrix[nx][ny] += dig
                visited[nx][ny] = True

T = int(input())

for tc in range(1,T+1):
    # 지도크기, 한번에 깎을 수 있는 크기
    N,K = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    # 출발지점 선정
    max_h = 0
    st_pos = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > max_h:
                max_h = matrix[i][j]
                st_pos.clear()
                st_pos.append((i,j))
            elif matrix[i][j] == max_h:
                st_pos.append((i,j))

    max_len = 0
    visited = [[True] * N for _ in range(N)]
    #print(st_pos)
    for i,j in st_pos:
        visited[i][j] = False
        find_max_len(i, j, True,1,visited)
        visited[i][j] = True

    print(f"#{tc} {max_len}")