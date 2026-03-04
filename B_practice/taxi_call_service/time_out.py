from typing import List
import heapq
from collections import deque


class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance


# 2차원 리스트, heapq 사용
matrix = []
# 도시 크기
town_n = 0
# 호출 최대 거리
max_l = -1
# 택시 정보 : 택시번호 : (좌표, 이동거리, 이송거리)
taxi_info = {}
# 최장 운송 정보 : heapq , (손님이송거리, 택시번호)
most_data = []

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(st_x, st_y, l):
    # 좌표, 거리
    queue = deque([((st_x, st_y), 0)])
    visited = [[False] * town_n for _ in range(town_n)]
    visited[st_x][st_y] = True
    in_area_taxi = []
    # 만약 시작지점에 택시가 이미 있다면
    if matrix[st_x][st_y]:
        # heapq이므로 0번 인덱스가 가장 최소값
        return matrix[st_x][st_y][0], (st_x, st_y)
    # 탐색 범위 변수
    last_distance = 0
    while queue:
        (x, y), dist = queue.popleft()
        # 거리가 최대 거리를 벗어나면 탐색 종료
        if dist > l:
            break
        # 일정 거리를 전부 순회한 결과가 있을 경우 탐색 종료
        if last_distance != dist and in_area_taxi:
            break
        last_distance = dist
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < town_n and 0 <= ny < town_n):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if dist + 1 <= l:
                if matrix[nx][ny]:
                    # 여러개가 있더라도, 0번째 인덱스가 이 지역에서 가장 번호가 작은 택시
                    in_area_taxi.append( (matrix[nx][ny][0], (nx,ny)) )
                queue.append(((nx, ny), dist + 1))

    # 거리를 벗어나거나 특정 범위 순회 후 택시 발견 시 빠져나옴
    if in_area_taxi:
        in_area_taxi.sort(key=lambda x: x[0])
        return in_area_taxi[0] # 택시번호, 좌표
    else:
        return -1


def init(N: int, M: int, L: int, mXs: List[int], mYs: List[int]) -> None:
    global matrix, town_n, max_l, taxi_info, most_data
    # 초기화
    town_n = N
    max_l = L

    matrix = [[[] for _ in range(N)] for _ in range(N)]
    taxi_info = {}
    most_data = []

    # 택시 정보 등록
    for i in range(M):
        taxi_info[i+1] = [(mXs[i], mYs[i]), 0, 0]
        heapq.heappush(matrix[mXs[i]][mYs[i]], i+1)
        heapq.heappush(most_data, (0, i + 1))


def pickup(mSX: int, mSY: int, mEX: int, mEY: int) -> int:
    # 출발지 x, 출발지 y, 도착지 x, 도착지 y
    result = bfs(mSX, mSY, max_l)
    if result == -1:
        return -1
    taxi_n, (taxi_x, taxi_y) = result

    dist_taxi_start = abs(taxi_x - mSX) + abs(taxi_y - mSY)
    dist_start_end = abs(mSX - mEX) + abs(mSY - mEY)

    # 택시 운송 정보 업데이트
    (old_x, old_y), total, custom = taxi_info[taxi_n]

    update_total = total + (dist_taxi_start + dist_start_end)
    update_custom = custom + dist_start_end

    taxi_info[taxi_n] = ((mEX, mEY), update_total, update_custom) # 택시 정보 업데이트 완료

    # 최장 운송 경로 등록
    heapq.heappush(most_data, (-update_custom, taxi_n))

    # matrix 좌표 갱싱
    heapq.heappop(matrix[taxi_x][taxi_y]) # 가장 작은 택시번호 pop
    heapq.heappush(matrix[mEX][mEY], taxi_n) # heapq로 택시 번호 push

    return taxi_n


def reset(mNo: int) -> Result:
    (x, y), total, custom = taxi_info[mNo]
    taxi_info[mNo] = [(x,y), 0, 0]

    heapq.heappush(most_data, (0, mNo))

    return Result(x, y, total, custom)


def getBest(mNos: List[int]) -> None:
    # 리턴할 택시 번호 갯수
    require_cnt = len(mNos)
    roll_back = []
    cnt = 0

    while most_data and cnt < require_cnt:
        # most_data는 최장 운송 경로를 음수로 받아 가장 작은 값을 먼저 출력함
        # 값이 같을 경우 전환 없이 받은 택시 번호가 가장 작은 값을 더 우선해서 출력함
        custom, taxi_n = heapq.heappop(most_data)

        # 실제 택시 데이터와 맞는지 확인
        real_custom = taxi_info[taxi_n][2]

        if -custom != real_custom:
            continue

        mNos[cnt] = taxi_n
        cnt += 1

        # 복구 데이터 백업
        roll_back.append((custom, taxi_n))

    for data in roll_back:
        heapq.heappush(most_data, data)























