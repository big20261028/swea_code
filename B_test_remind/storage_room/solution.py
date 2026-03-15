from heapq import heappop,heappush

class Point():
    def __init__(self, y=0, x=0):
        self.y = y
        self.x = x

class RESULT():
    def __init__(self):
        self.p = [ Point() for _ in range(5) ]

room_n = 0
sector_n = 0

bucket_n = 0
buckets = [[]]
bucket_increase = [[0]]

matrix = [[]]

def init(N, K, mPlane):
    global room_n, sector_n, bucket_n, buckets, bucket_increase, matrix

    room_n = N # N은 항상 K로 나눈 나머지가 0
    sector_n = K # K는 N의 약수

    bucket_n = N//K
    buckets = [ [ list() for _ in range(bucket_n) ] for _ in range(bucket_n) ]
    bucket_increase = [ [0] * bucket_n for _ in range(bucket_n) ]

    matrix = [ [0] * N for _ in range(N) ]

    for y in range(N):
        for x in range(N):
            matrix[y][x] = mPlane[y][x]
            by, bx = y // sector_n, x // sector_n
            heappush(buckets[by][bx], (-mPlane[y][x], x, y)) # 우선순위: 재고 많은순, x좌표 작은순, y좌표 작은순

# 좌상단 좌표, 우하단 좌표, 가져올 갯수
def query(A,B,mCount):
    st_y, st_x = A.y, A.x
    end_y, end_x = B.y, B.x

    bsy, bsx = st_y // sector_n, st_x // sector_n
    bey, bex = end_y // sector_n, end_x // sector_n

    visited = set() # 이게 없어서 망한듯
    temp_list = []
    repair = []
    for by in range(bsy, bey + 1):
        for bx in range(bsx, bex + 1):
            while buckets[by][bx]:
                stack, x, y = heappop(buckets[by][bx])

                if stack != -matrix[y][x]:
                    continue
                if (y,x) in visited:
                    continue

                real_val = stack - bucket_increase[by][bx]

                heappush(temp_list, (real_val, x, y, (by,bx)))
                repair.append((stack, x, y, (by,bx)))
                visited.add((y,x))
                break

    candidate_list = []
    # 여기서 코드가 자꾸 터져서 while temp_list and len(candidate_list) < mCount로 바꿔서 제출함
    while len(candidate_list) < mCount:
        real_val, x, y, (by, bx) = heappop(temp_list)
        candidate_list.append((real_val, x, y))

        while buckets[by][bx]:
            next_val, nx, ny = heappop(buckets[by][bx])

            if next_val != -matrix[ny][nx]:
                continue
            if (ny, nx) in visited:
                continue

            next_real_val = next_val - bucket_increase[by][bx]

            heappush(temp_list, (next_real_val, nx, ny, (by,bx)))
            repair.append((next_val, nx, ny, (by,bx)))
            visited.add((y, x))
            break

    while repair:
        val, x, y, (by, bx) = repair.pop()
        heappush(buckets[by][bx], (val, x, y))

    result = RESULT()
    candidate_list.sort()

    for i, item in enumerate(candidate_list):
        point = result.p[i]
        point.y = item[2]
        point.x = item[1]

    return result

def get_value(P):
    y, x = P.y, P.x
    by, bx = y // sector_n, x // sector_n

    real_val = matrix[y][x] + bucket_increase[by][bx]
    return real_val


def set_value(P, mVal):
    y, x = P.y, P.x
    by, bx = y // sector_n, x // sector_n
    # 데이터를 빼올때 bucket_increase 값을 더해서 나와야 하므로 그 값만큼 빼서 넣어두기
    calculated_val = mVal - bucket_increase[by][bx]
    matrix[y][x] = calculated_val
    heappush(buckets[by][bx], (-calculated_val, x, y))


def increase_val(A,B,mIncrease):
    st_y, st_x = A.y, A.x
    end_y, end_x = B.y, B.x

    bsy, bsx = st_y // sector_n, st_x // sector_n
    bey, bex = end_y // sector_n, end_x // sector_n

    for by in range(bsy, bey + 1):
        for bx in range(bsx, bex + 1):
            bucket_increase[by][bx] += mIncrease