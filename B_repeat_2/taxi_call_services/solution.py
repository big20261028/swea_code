from typing import List
from heapq import heappush, heappop

class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance

city_n = 0
call_l = 0
taxi_info = {} # taxi_n : [(x,y), total, custom]
buckets = [[]] # [x][y] = {taxi_n, taxi_n, taxi_n ......}
bucket_size = 0
most_drive_taxis = [] # [ (custom, taxi_n) , ......]

def init(N : int, M : int, L : int, mXs : List[int], mYs : List[int]) -> None:
    global city_n, call_l, taxi_info, buckets, most_drive_taxis, bucket_size

    city_n = N
    call_l = L
    taxi_info = {}
    most_drive_taxis = []
    bucket_size = N//L + 1
    buckets = [ [ set() for _ in range(bucket_size) ] for _ in range(bucket_size) ]


    for i in range(M):
        taxi_info[i+1] = [ (mXs[i], mYs[i]), 0, 0 ]
        bx = mXs[i] // L
        by = mYs[i] // L
        buckets[bx][by].add(i+1)
        heappush(most_drive_taxis, (0, i+1))


def pickup(mSX : int, mSY : int, mEX : int, mEY : int) -> int:
    bsx, bsy = mSX // call_l, mSY // call_l

    min_taxi_n = float('inf')
    min_dist = float('inf')

    for dx in range(-1,2):
        for dy in range(-1,2):
            bnx, bny = bsx + dx, bsy + dy
            if not (0 <= bnx < bucket_size and 0 <= bny < bucket_size):
                continue
            for taxi_n in buckets[bnx][bny]:
                (t_x, t_y), total, custom = taxi_info[taxi_n]
                dist = abs(t_x - mSX) + abs(t_y - mSY)
                if dist > call_l:
                    continue

                if min_dist > dist:
                    min_taxi_n = taxi_n
                    min_dist = dist
                elif min_dist == dist and min_taxi_n > taxi_n:
                    min_taxi_n = taxi_n

    if min_dist == float('inf'):
        return -1

    dist_taxi_st = min_dist
    dist_st_end = abs(mSX - mEX) + abs(mSY - mEY)

    # 택시 정보 갱신
    (t_x, t_y), old_total, old_custom = taxi_info[min_taxi_n]

    new_total = old_total + (dist_taxi_st + dist_st_end)
    new_custom = old_custom + dist_st_end

    taxi_info[min_taxi_n] = [ (mEX, mEY), new_total, new_custom ]

    # 버킷 갱신
    bx, by = t_x // call_l, t_y // call_l
    bnx, bny = mEX // call_l, mEY // call_l

    buckets[bx][by].remove(min_taxi_n)
    buckets[bnx][bny].add(min_taxi_n)

    # mvp 택시 정보 갱신
    heappush(most_drive_taxis, (-new_custom, min_taxi_n))

    return min_taxi_n


def reset(mNo : int) -> Result:
    (t_x, t_y), total, custom = taxi_info[mNo]
    taxi_info[mNo] = [ (t_x, t_y), 0, 0 ]

    heappush(most_drive_taxis, (0, mNo))

    return Result(t_x, t_y, total, custom)

def getBest(mNos : List[int]) -> None:

    mvp_taxis = []
    repair = []

    while most_drive_taxis and len(mvp_taxis) < 5:
        custom, taxi_n = heappop(most_drive_taxis)

        real_custom = taxi_info[taxi_n][2]

        if -custom != real_custom:
            continue
        if taxi_n in mvp_taxis:
            continue

        mvp_taxis.append(taxi_n)
        repair.append((custom, taxi_n))

    for custom, taxi_n in repair:
        heappush(most_drive_taxis, (custom, taxi_n))

    for idx, taxi_n in enumerate(mvp_taxis):
        mNos[idx] = taxi_n

    # print(city_n, call_l, bucket_size)
    # print(taxi_info)
    # print(buckets)
    # print(most_drive_taxis)
    # print('------')
    # print('결과값', mvp_taxis)
    # print('------')