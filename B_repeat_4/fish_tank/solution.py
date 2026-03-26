from typing import List
from collections import defaultdict

class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0


class FishTank:
    def __init__(self, tank_id, width, height, lengths, up_shapes):
        self.tank_id = tank_id
        self.width = width
        self.height = height
        self.lengths = list(lengths)
        self.up_shapes = list(up_shapes)
        self.subset_up_shapes = defaultdict(list)
        self.water_need_data = [0] * (height + 1)
        self.cal_water_need()
        self.cal_subset_up_shapes()


    def cal_water_need(self):
        water_h = [0] * (self.height + 1)
        for h in self.lengths:
            if h > self.height: continue
            water_h[h] += 1

        water_need = 0
        total_need = 0
        for h in range(1, self.height + 1):
            water_need += water_h[h-1]
            total_need += water_need
            self.water_need_data[h] = total_need


    def cal_subset_up_shapes(self):
        self.subset_up_shapes = defaultdict(list)
        for i in range(self.width - 2):
            up_shape_subset = (self.up_shapes[i], self.up_shapes[i+1], self.up_shapes[i+2])
            self.subset_up_shapes[up_shape_subset].append(i)


    def is_can_install(self,col, lengths):
        l_1 = self.lengths[col]
        l_2 = self.lengths[col+1]
        l_3 = self.lengths[col+2]
        extended_l_1 = l_1 + lengths[0]
        extended_l_2 = l_2 + lengths[1]
        extended_l_3 = l_3 + lengths[2]

        if extended_l_1 > self.height or extended_l_2 > self.height or extended_l_3 > self.height:
            return False

        if extended_l_1 <= l_2 or extended_l_3 <= l_2:
            return False
        elif extended_l_2 <= l_1 or extended_l_2 <= l_3:
            return False

        return True


    def do_install(self, col, lengths, up_shapes):

        for i in range(3):
            self.lengths[col + i] += lengths[i]
            self.up_shapes[col + i] = up_shapes[i]

        self.cal_subset_up_shapes()
        self.cal_water_need()


tank_list = []

def init(N: int, mWidth: int, mHeight: int, mIDs: List[int], mLengths: List[List[int]], mUpShapes: List[List[int]]) -> None:
    global tank_list
    tank_list = []

    for i in range(N):
        tank = FishTank(mIDs[i], mWidth, mHeight, mLengths[i], mUpShapes[i])
        tank_list.append(tank)

    tank_list.sort(key=lambda x:x.tank_id)


def checkStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:
    total_cnt = 0

    target_subset = ( mDownShapes[0], mDownShapes[1], mDownShapes[2] )
    for tank in tank_list:
        if target_subset in tank.subset_up_shapes:
            for col in tank.subset_up_shapes[target_subset]:
                if tank.is_can_install(col, mLengths):
                    total_cnt += 1

    return total_cnt

def addStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:
    target_subset = ( mDownShapes[0], mDownShapes[1], mDownShapes[2] )
    for tank in tank_list:
        if target_subset in tank.subset_up_shapes:
            for col in tank.subset_up_shapes[target_subset]:
                if tank.is_can_install(col, mLengths):
                    tank.do_install(col, mLengths, mUpShapes)
                    result = (tank.tank_id * 1000) + col + 1
                    return result

    return 0

def pourIn(mWater: int) -> Result:
    rs_id, rs_h, rs_used = 0, 0, 0

    for tank in tank_list:
        max_h = 0
        max_used = 0

        top, bottom = tank.height, 1
        while bottom <= top:
            middle = (top + bottom) // 2
            need_water_val = tank.water_need_data[middle]
            if 0 < need_water_val <= mWater:
                max_h = middle
                max_used = need_water_val
                bottom = middle + 1
            else:
                if need_water_val == 0 and bottom < top:
                    bottom = middle + 1
                else:
                    top = middle - 1

        if max_h > rs_h:
            rs_id, rs_h, rs_used = tank.tank_id, max_h, max_used
        elif max_h == rs_h and max_used > rs_used:
            rs_id, rs_used = tank.tank_id, max_used
        # 아이디가 더 작은 경우는 이미 아이디가 작은 순서대로 정렬되어 있으므로 검사하지 않음

    ret = Result()
    ret.ID, ret.height, ret.used = rs_id, rs_h, rs_used
    return ret
