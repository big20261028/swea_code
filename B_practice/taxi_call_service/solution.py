from typing import List
import heapq
from collections import deque


class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance


# 버킷
buckets = []
# 도시 크기
town_n = 0
# 호출 최대 거리
max_l = -1
# 택시 정보 : 택시번호 : (좌표, 이동거리, 이송거리)
taxi_info = {}
# 최장 운송 정보 : heapq , (손님이송거리, 택시번호)
most_data = []


def init(N: int, M: int, L: int, mXs: List[int], mYs: List[int]) -> None:
    global buckets, town_n, max_l, taxi_info, most_data
    # 초기화
    town_n = N
    max_l = L

    taxi_info.clear()
    most_data.clear()

    # 전체 크기를 전체 범위만큼의 크기로 잘라서 큼직하게 저장
    grid_size = (N // L) + 1
    # 택시 좌표도 L으로 나눠서 저장
    # 나중에 검사할때 taxi_info로 정확한 좌표값 가져와서 유효한지 검사
    # 추가 제거 편리하도록 set으로 저장
    buckets = [[set() for _ in range(grid_size)] for _ in range(grid_size)]

    # 택시 정보 등록
    for i in range(M):
        taxi_n = i + 1
        x, y = mXs[i], mYs[i]

        taxi_info[taxi_n] = [(x, y), 0, 0]
        buckets[x // L][y // L].add(taxi_n)
        heapq.heappush(most_data, (0, taxi_n))


def pickup(mSX: int, mSY: int, mEX: int, mEY: int) -> int:
    min_dist = float('inf')
    min_taxi_n = -1

    # 출발지가 속한 버킷 좌표
    bx = mSX // max_l
    by = mSY // max_l
    grid_size = len(buckets)

    for dbx in range(-1, 2):
        for dby in range(-1, 2):
            nbx, nby = bx + dbx, by + dby

            # 맵 범위를 벗어나지 않는 버킷만 확인
            if 0 <= nbx < grid_size and 0 <= nby < grid_size:
                # 해당 구역에 있는 모든 택시 목록 조회
                for taxi_n in buckets[nbx][nby]:
                    tx, ty = taxi_info[taxi_n][0]
                    dist = abs(tx - mSX) + abs(ty - mSY)

                    # 호출 최대 거리 초과면 패스
                    if dist > max_l:
                        continue

                    # 가장 가깝거나, 거리가 같을 때 번호가 작은 택시 선정
                    if dist < min_dist:
                        min_dist = dist
                        min_taxi_n = taxi_n
                    elif dist == min_dist:
                        if taxi_n < min_taxi_n:
                            min_taxi_n = taxi_n

    # 조건에 맞는 택시가 없으면 종료
    if min_taxi_n == -1:
        return -1

    # 선정된 택시 정보 업데이트 로직
    (tx, ty), total, custom = taxi_info[min_taxi_n]

    dist_start_end = abs(mSX - mEX) + abs(mSY - mEY)
    move_dist = min_dist + dist_start_end

    update_total = total + move_dist
    update_custom = custom + dist_start_end

    taxi_info[min_taxi_n] = [(mEX, mEY), update_total, update_custom]

    # 버킷 데이터 갱신
    buckets[tx // max_l][ty // max_l].remove(min_taxi_n)
    buckets[mEX // max_l][mEY // max_l].add(min_taxi_n)

    # 최장 운송 경로 등록
    heapq.heappush(most_data, (-update_custom, min_taxi_n))

    return min_taxi_n


def reset(mNo: int) -> Result:
    (x, y), total, custom = taxi_info[mNo]
    taxi_info[mNo] = [(x,y), 0, 0]

    heapq.heappush(most_data, (0, mNo))

    return Result(x, y, total, custom)


def getBest(mNos: List[int]) -> None:
    # 리턴할 택시 번호 갯수
    require_cnt = len(mNos)
    roll_back = []
    visited = set()
    cnt = 0

    while most_data and cnt < require_cnt:
        # most_data는 최장 운송 경로를 음수로 받아 가장 작은 값을 먼저 출력함
        # 값이 같을 경우 전환 없이 받은 택시 번호가 가장 작은 값을 더 우선해서 출력함
        custom, taxi_n = heapq.heappop(most_data)

        if taxi_n in visited:
            continue

        # 실제 택시 데이터와 맞는지 확인
        real_custom = taxi_info[taxi_n][2]
        if -custom != real_custom:
            continue

        visited.add(taxi_n)
        mNos[cnt] = taxi_n
        cnt += 1

        # 복구 데이터 백업
        roll_back.append((custom, taxi_n))

    for data in roll_back:
        heapq.heappush(most_data, data)























