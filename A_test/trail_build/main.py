import sys
sys.stdin = open('sample_input.txt','r')

'''
주의사항
시작지점부터 깎으며 시작할 수 있다.
꼭 가장 높은 곳에서 멈추진 않는다.
'''

import heapq

# 순서가 있는 큐를 사용하면 쉽게 구할 수 있나?
# 모든 경로를 탐색하는 수 밖에 없나

dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]

# 시작지점을 깎아본 상태, 안깎아본 상태 두개 해보면 된다
# 매개변수 : 거리, 시작지점, 큐, 깎기, 방문 데이터
def search_short_pass(deps,pos,flag,visited):
    global max_load
    # 더이상 올라갈 길이 없으면
    # 걸어온 거리가 최대값인지 확인
    # 아직 안깎았을때 / 깎으면 오히려 올라갈 수 있던 길이 올라갈 수 없어지니 굳이 깎아볼 필요는 없다
    # if flag:
    #     for dig in range(1,K+1):
    #         for dx,dy in dxy:
    #             nx = pos[0] + dx
    #             ny = pos[1] + dy
    #             if 0 <= nx < N and 0 <= ny < N :
    #                 if visited[nx][ny] and matrix[nx][ny]-dig > matrix[pos[0]][pos[1]]:
    #                     break
    #         else:
    #             # break 안걸리면 도달
    #             # 갈 수 있는 곳이 한곳도 없다
    #             max_load = max_reward(max_load, deps)
    #             return
    # # 깎았을때
    # else:
    for dx,dy in dxy:
        nx = pos[0] + dx
        ny = pos[1] + dy
        if 0 <= nx < N and 0 <= ny < N :
            if visited[nx][ny] and matrix[nx][ny] < matrix[pos[0]][pos[1]]:
                break
    else:
        # break 안걸리면 도달
        # 갈 수 있는 곳이 한곳도 없다
        max_load = max(max_load, deps)
        return


    # 아직 지형을 안깎았을때, 다음경로를 깎아보고
    if flag:
        for dig in range(1, K + 1):
            for dx, dy in dxy:
                nx = pos[0] + dx
                ny = pos[1] + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny] and matrix[nx][ny]-dig < matrix[pos[0]][pos[1]]:
                        matrix[nx][ny] -= dig
                        visited[nx][ny] = False
                        search_short_pass(deps + 1, [nx,ny], False,visited)
                        visited[nx][ny] = True
                        matrix[nx][ny] += dig

    # 안깎아본다 / True로 들어오면 둘다 해보고 False로 들어오면 안깎아보는것만 해봄
    for dx,dy in dxy:
        nx = pos[0] + dx
        ny = pos[1] + dy
        if 0 <= nx < N and 0 <= ny < N :
            if visited[nx][ny] and matrix[nx][ny] < matrix[pos[0]][pos[1]]:
                visited[nx][ny] = False
                search_short_pass(deps+1,[nx,ny],True,visited)
                visited[nx][ny] = True

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    # 시작지점 선정
    # 가장 높은 봉우리가 얼마 값인지, 몇 개소 있는지 확인
    min_h = float('inf')
    max_h = float('-inf')
    st_pos = []
    for i in range(N):
        for j in range(N):
            if max_h < matrix[i][j]:
                max_h = matrix[i][j]
                st_pos.clear()
                st_pos.append([i,j])
            elif max_h == matrix[i][j]:
                st_pos.append([i, j])

            min_h = min(max_h, matrix[i][j])

    # print(min_h)
    # print(st_pos)
    visited = [ list(True for _ in range(N)) for _ in range(N) ]
    hq = []
    max_load = float('-inf')

    # 시작지점 별 최단거리 구하기
    for pos in st_pos:
        search_short_pass(0,pos,True,visited)
        search_short_pass(0,pos,False,visited)

    print(f'#{tc} {max_load}')