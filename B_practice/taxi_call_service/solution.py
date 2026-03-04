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
    queue = deque([[(st_x, st_y), 0]])
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
        # 최장 운송 정보는 굳이 등록할 필요 X


def pickup(mSX: int, mSY: int, mEX: int, mEY: int) -> int:
    return -1


def reset(mNo: int) -> Result:
    return Result(-1, -1, -1, -1)


def getBest(mNos: List[int]) -> None:
    pass
