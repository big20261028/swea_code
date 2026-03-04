from typing import List
import heapq
from collections import deque
'''
택시가 한 장소에 여러개 있을 경우 있음 
수정필요
'''
class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance

# 도시 좌표
matrix = []
# 도시 크기
town_N = 0
# 호출 받을 수 있는 최대 거리
max_L = -1
# 택시 정보 / 택시번호 : (총 이동거리, 손님 이송거리, 택시 좌표)
taxi_infos = {}
# 거리가 가장 큰 순서 뽑기 위한 heapq
# ( ( - (손님 이송거리 ) ) ,총이동거리 ,택시번호
heap_datas = []

dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]

def bfs(st_pos, l, N):
    queue = deque([[st_pos[0], st_pos[1], 0]])
    visited = [[False] * N for _ in range(N)]
    visited[st_pos[0]][st_pos[1]] = True
    in_area_taxi = []
    if matrix[st_pos[0]][st_pos[1]]:
        matrix[st_pos[0]][st_pos[1]].sort()
        return matrix[st_pos[0]][st_pos[1]][0], (st_pos[0], st_pos[1])
    last_distance = 0
    while queue:
        x, y, dts = queue.popleft()
        if dts > l:
            break
        if last_distance != dts and in_area_taxi:
            break
        last_distance = dts
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if matrix[nx][ny]:
                for n in matrix[nx][ny]:
                    in_area_taxi.append((n, (nx, ny)))
            queue.append([nx, ny, dts + 1])

    if in_area_taxi:
        in_area_taxi.sort(key=lambda x: x[0])
        return in_area_taxi[0]
    else:
        return -1

def init(N : int, M : int, L : int, mXs : List[int], mYs : List[int]) -> None:
    global matrix, max_L, taxi_infos, town_N

    matrix = [ [ deque() for _ in range(N) ]  for _ in range(N)]
    heap_datas = []
    max_L = L
    taxi_infos = {}
    town_N = N
    for i in range(M):
        taxi_infos[i+1] = (0, 0, (mXs[i], mYs[i]))
        matrix[mXs[i]][mYs[i]].append(i+1)
        heapq.heappush(heap_datas, (0, 0, i+1))

def pickup(mSX : int, mSY : int, mEX : int, mEY : int) -> int:
    # 출발지 x, 출발지 y, 도착지 x, 도착지 y
    result = bfs((mSX,mSY),max_L,town_N)
    if result == -1:
        return -1
    taxi_n, taxi_pos = result
    dist_taxi_start = abs(taxi_pos[0] - mSX) + abs(taxi_pos[1] - mSY)
    dist_start_end = abs(mSX - mEX) + abs(mSY - mEY)

    taxi_total, taxi_total_custom, (taxi_x, taxi_y) = taxi_infos[taxi_n]

    new_total = taxi_total + (dist_taxi_start + dist_start_end)
    new_custom = taxi_total_custom + dist_start_end

    taxi_infos[taxi_n] = (new_total, new_custom, (mEX, mEY))

    heapq.heappush(heap_datas, (-new_custom, new_total, taxi_n))

    matrix[taxi_x][taxi_y].pop()
    matrix[mEX][mEY] = taxi_n

    return taxi_n

def reset(mNo : int) -> Result:
    total, custom, (x, y) = taxi_infos[mNo]
    taxi_infos[mNo] = (0, 0, (x, y))

    heapq.heappush(heap_datas, (0, 0, mNo))

    return Result(x, y, total, custom)

def getBest(mNos : List[int]) -> None:

    pass