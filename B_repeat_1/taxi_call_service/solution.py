from typing import List
from heapq import heappush,heappop,heapify

class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance


# 택시번호 1 ~ M : ( (x,y), 이동거리, 이송거리  )
taxi_info = {}
# 도시 한변의 길이
n = 0
# 호출받을 수 있는 택시의 최대 거리
l = 0
# 버킷
buckets = []
# 가장 많이 운행한 택시 정보 ( heap )
# (이송거리, 택시번호)
hq_taxi = []


def init(N: int, M: int, L: int, mXs: List[int], mYs: List[int]) -> None:
    global taxi_info, n, l, buckets, hq_taxi

    n = N
    l = L
    buckets = [ [set() for _ in range(N//L + 1)] for _ in range(N//L + 1) ]
    taxi_info.clear()
    hq_taxi.clear()

    # 택시 번호는 1부터 시작
    for i in range(M):
        bx = mXs[i] // L
        by = mYs[i] // L
        taxi_n = i + 1
        taxi_info[taxi_n] = [ (mXs[i],mYs[i]), 0, 0 ]
        heappush(hq_taxi, (0, taxi_n))
        buckets[bx][by].add(taxi_n)


def pickup(mSX: int, mSY: int, mEX: int, mEY: int) -> int:
    bsx, bsy = mSX // l, mSY // l

    min_dist = float('inf')
    min_taxi_n = 0

    # 버킷 좌표 주위 8방향 조회
    for dx in range(-1,2):
        for dy in range(-1,2):
            bnx, bny = bsx + dx, bsy + dy

            if not (0 <= bnx <= n//l and 0 <= bny <= n//l):
                continue

            for taxi_n in buckets[bnx][bny]:
                taxi_x, taxi_y = taxi_info[taxi_n][0]
                distance = abs(taxi_x - mSX) + abs(taxi_y - mSY)
                if distance > l: continue

                if min_dist > distance:
                    min_dist = distance
                    min_taxi_n = taxi_n
                elif min_dist == distance and min_taxi_n > taxi_n:
                    min_taxi_n = taxi_n

    # 호출 결과값 없을 경우 리턴
    if min_taxi_n == 0:
        return -1

    # 호출한 택시 이용 처리
    dist_taxi_st = min_dist
    dist_st_end = abs(mSX - mEX) + abs(mSY - mEY)

    total_dist = dist_taxi_st + dist_st_end
    customer_dist = dist_st_end

    # 택시 정보 갱신
    (ox,oy), old_total, old_custom = taxi_info[min_taxi_n]
    taxi_info[min_taxi_n] = [ (mEX,mEY), old_total + total_dist, old_custom + customer_dist ]

    # 버킷 위치 갱신
    bx, by = mEX // l, mEY // l
    box, boy = ox // l, oy // l
    buckets[box][boy].remove(min_taxi_n)
    buckets[bx][by].add(min_taxi_n)

    # 최대값 계산을 위한 힙 갱신
    heappush(hq_taxi, (-(old_custom + customer_dist), min_taxi_n))

    return min_taxi_n


def reset(mNo: int) -> Result:
    (ox,oy), total, custom = taxi_info[mNo]
    taxi_info[mNo] = [ (ox,oy), 0, 0 ]

    heappush(hq_taxi,(0, mNo))

    return Result(ox, oy, total, custom)


def getBest(mNos: List[int]) -> None:
    mvp_taxis = []
    require_cnt = len(mNos)
    repair = []

    hq = hq_taxi
    while hq and len(mvp_taxis) < require_cnt:
        custom_dist, taxi_n = heappop(hq)

        (rx,ry), real_total_dist, real_custom_dist = taxi_info[taxi_n]

        if -custom_dist != real_custom_dist:
            continue
        if taxi_n in mvp_taxis:
            continue

        mvp_taxis.append(taxi_n)
        repair.append((custom_dist, taxi_n))

    for item in repair:
        heappush(hq, item)

    for i in range(len(mvp_taxis)):
        mNos[i] = mvp_taxis[i]
