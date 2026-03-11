from typing import List

from collections import defaultdict


class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0

class FishTank:
    def __init__(self, Mid, width, height, lengths, shapes):
        self.Mid = Mid
        self.width = width
        self.height = height
        self.lengths = list(lengths)
        self.shapes = list(shapes)
        self.shapes_subset = defaultdict(list)
        self.water_need = [0] * (height + 1)
        self.cal_need_water()
        self.cal_shape_subset()

    def cal_need_water(self):
        h_water = [0] * (self.height + 1)
        for h in self.lengths:
            if h <= self.height:
                h_water[h] += 1

        can_fill_waters = 0
        total = 0
        for j in range(1, self.height + 1):
            can_fill_waters += h_water[j-1]
            total += can_fill_waters
            self.water_need[j] = total

    def cal_shape_subset(self):
        self.shapes_subset = defaultdict(list)

        for i in range(self.width - 2):
            sp_subset = (self.shapes[i], self.shapes[i+1], self.shapes[i+2])
            self.shapes_subset[sp_subset].append(i)

    # 이 어항 객체에 블록을 설치할 수 있는지 확인
    # shapes_subset에 없으면 리턴 -1
    # 있으면 해당 인덱스의 블록 높이 + 설치블록
    # 설치 조건 만족하는지 확인
    # 만족하는 col 인덱스 반환/
    def is_can_install(self, block_lengths, block_up_shapes, block_down_shapes):
        if tuple(block_down_shapes) not in self.shapes_subset:
            return -1

        for col in self.shapes_subset[tuple(block_down_shapes)]:
            if self.check_block_condition(col,block_lengths):
                return col

        return -1

    def check_block_condition(self, col_idx, block_lengths):
        l_1 = self.lengths[col_idx] + block_lengths[0]
        l_2 = self.lengths[col_idx + 1] + block_lengths[1]
        l_3 = self.lengths[col_idx + 2] + block_lengths[2]

        if l_1 > self.height or l_2 > self.height or l_3 > self.height:
            return False

        if l_1 <= self.lengths[col_idx + 1] or l_3 <= self.lengths[col_idx + 1]:
            return False
        if l_2 <= self.lengths[col_idx] or l_2 <= self.lengths[col_idx + 2]:
            return False

        return True

    def do_install(self, col, block_lengths, block_up_shapes, block_down_shapes):

        for i in range(3):
            self.lengths[col + i] += block_lengths[i]
            self.shapes[col + i] = block_up_shapes[i]


        self.cal_shape_subset()
        self.cal_need_water()

        return True

tank_list = []

def init(N: int, mWidth: int, mHeight: int, mIDs: List[int], mLengths: List[List[int]], mUpShapes: List[List[int]]) -> None:
    global tank_list
    tank_list = []
    for i in range(N):
        tank = FishTank(mIDs[i], mWidth, mHeight, mLengths[i], mUpShapes[i])
        tank_list.append(tank)
    tank_list.sort(key=lambda x : x.Mid)


def checkStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:
    cnt = 0

    for tank in tank_list:
        if tuple(mDownShapes) in tank.shapes_subset:
            for col in tank.shapes_subset[tuple(mDownShapes)]:
                if tank.check_block_condition(col,mLengths):
                    cnt += 1

    return cnt

def addStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:

    for tank in tank_list:
        if tuple(mDownShapes) in tank.shapes_subset:
            for col in tank.shapes_subset[tuple(mDownShapes)]:
                if tank.check_block_condition(col,mLengths):
                    tank.do_install(col,mLengths,mUpShapes,mDownShapes)
                    result = (tank.Mid * 1000) + (col+1)
                    return result
    return 0

def pourIn(mWater: int) -> Result:
    rs_Mid, rs_h, rs_wt = 0,0,0

    for tank in tank_list:
        top_idx = tank.height
        bottom_idx = 1 # 탱크 높이는 1부터 height까지

        max_water_need = 0
        max_height = 0
        while bottom_idx <= top_idx:
            middle_idx = (top_idx + bottom_idx) // 2
            need = tank.water_need[middle_idx]

            if 0 < need <= mWater:
                max_height = middle_idx
                max_water_need = need
                bottom_idx = middle_idx + 1
            else:
                if need == 0 and middle_idx < tank.height:
                    bottom_idx = middle_idx + 1
                else:
                    top_idx = middle_idx - 1

        if max_height > rs_h:
            rs_Mid, rs_h, rs_wt = tank.Mid, max_height, max_water_need

        elif max_height > 0 and max_height == rs_h and max_water_need > rs_wt:
            rs_Mid, rs_wt = tank.Mid, max_water_need

    ret = Result()
    ret.ID , ret.height , ret.used = rs_Mid, rs_h, rs_wt
    return ret
