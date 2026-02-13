import sys
sys.stdin = open('sample_input.txt','r')
'''
갈 곳이 없으면 자동으로 끝난다 - > 그냥 매번 최대 길이를 갱신하면 됨
현재 flag 변수를 넘겨줘야 한다
'''
dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]

def is_in_range(x,y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def find_short_path(deps,pos,visited,flag):
    global max_load

    max_load = max(max_load, deps)

    if flag:
        for dig in range(1,K+1):
            for dx,dy in dxy:
                nx = pos[0] + dx
                ny = pos[1] + dy
                if is_in_range(nx, ny) and visited[nx][ny] and matrix[nx][ny]-dig < matrix[pos[0]][pos[1]]:
                    matrix[nx][ny] -= dig
                    visited[nx][ny] = False
                    find_short_path(deps+1,[nx,ny],visited,False)
                    matrix[nx][ny] += dig
                    visited[nx][ny] = True

    for dx,dy in dxy:
        nx = pos[0] + dx
        ny = pos[1] + dy
        if is_in_range(nx,ny) and visited[nx][ny] and matrix[nx][ny] < matrix[pos[0]][pos[1]]:
            visited[nx][ny] = False
            find_short_path(deps+1,[nx,ny],visited,flag)
            visited[nx][ny] = True

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    max_h = float('-inf')
    st_pos = []
    for i in range(N):
        for j in range(N):
            if max_h < matrix[i][j]:
                max_h = matrix[i][j]
                st_pos.clear()
                st_pos.append([i,j])
            elif max_h == matrix[i][j]:
                st_pos.append([i,j])

    visited = [ list(True for _ in range(N)) for _ in range(N)]
    max_load = 0

    for pos in st_pos:
        visited[pos[0]][pos[1]] = False
        find_short_path(1,pos,visited,True)
        visited[pos[0]][pos[1]] = True

    print(f'#{tc} {max_load}')