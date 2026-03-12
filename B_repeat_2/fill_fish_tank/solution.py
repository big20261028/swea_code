from typing import List
from collections import defaultdict

class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0

class FishTank:
    def __init__(self,t_id, t_w, t_h, block_lengths, up_shapes):
        self.t_id = t_id
        self.t_w = t_w
        self.t_h = t_h
        self.block_lengths = list(block_lengths)
        self.up_shapes = list(up_shapes)
        self.subset_up_shape = defaultdict(list) #(up1,up2,up3) : [ col_idx, col_idx ....]
        self.need_waters = [0] * (t_h + 1) # 인덱스0은 바닥
        self.cal_subset()
        self.cal_need_waters()

    def cal_need_waters(self):
        water_by_h = [0] * (self.t_h + 1)
        for h in self.block_lengths:
            if h <= self.t_h:
                water_by_h[h] += 1

        water_need_val = 0
        total_need = 0
        for h in range(1,(self.t_h + 1)): # 인덱스 t_h 까지 탐색해야하므로
            water_need_val += water_by_h[h-1]
            total_need += water_need_val
            self.need_waters[h] = total_need
        #print(self.need_waters)

    def cal_subset(self):
        self.subset_up_shape = defaultdict(list)

        for col in range(self.t_w - 2):
            subset_item = (self.up_shapes[col], self.up_shapes[col+1], self.up_shapes[col+2])
            self.subset_up_shape[subset_item].append(col) # 우선순위 순서대로 들어감
        #print(self.subset_up_shape)

    def can_install(self,col, block_lengths, up_shapes, down_shapes):
        l_1 = self.block_lengths[col]
        l_2 = self.block_lengths[col+1]
        l_3 = self.block_lengths[col+2]

        install_l_1 = l_1 + block_lengths[0]
        install_l_2 = l_2 + block_lengths[1]
        install_l_3 = l_3 + block_lengths[2]

        if install_l_1 > self.t_h or install_l_2 > self.t_h or install_l_3 > self.t_h:
            return False

        if install_l_1 <= l_2:
            return False
        if install_l_2 <= l_1 or install_l_2 <= l_3:
            return False
        if install_l_3 <= l_2:
            return False
        #print('install ok')
        return True

    def install_block(self, col, block_lengths, up_shapes, down_shapes):
        for i in range(3):
            self.block_lengths[col+i] += block_lengths[i]
            self.up_shapes[col+i] = up_shapes[i]

        self.cal_subset()
        self.cal_need_waters()
        #print('블록설치완료')


tank_list = []

def init(N: int, mWidth: int, mHeight: int, mIDs: List[int], mLengths: List[List[int]], mUpShapes: List[List[int]]) -> None:
        global tank_list
        tank_list = []

        for i in range(N):
            tank = FishTank(mIDs[i],mWidth,mHeight,mLengths[i],mUpShapes[i])
            tank_list.append(tank)

        tank_list.sort(key=lambda x:x.t_id)

def checkStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:
    join_subset = (mDownShapes[0], mDownShapes[1], mDownShapes[2])

    cnt = 0

    for tank in tank_list:
        # 하판 조합이 탱크에 있는지 확인
        if join_subset in tank.subset_up_shape:
            # 해당 하판 조합이 위치한 col들로 순회
            for col in tank.subset_up_shape[join_subset]:
                # 길이가 넘어가지 않는지 확인
                if tank.can_install(col, mLengths, mUpShapes, mDownShapes):
                    cnt += 1

    return cnt

def addStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:
    join_subset = (mDownShapes[0], mDownShapes[1], mDownShapes[2])

    for tank in tank_list:
        # 하판 조합이 탱크에 있는지 확인
        if join_subset in tank.subset_up_shape:
            # 해당 하판 조합이 위치한 col들로 순회
            for col in tank.subset_up_shape[join_subset]:
                # 길이가 넘어가지 않는지 확인
                if tank.can_install(col, mLengths, mUpShapes, mDownShapes):
                    # 탱크는 id순으로, 하판 조합은 작은 col 인덱스 순으로 정렬되어 있음
                    # 가장 첫번째로 if문을 통과한 장소에 바로 설치
                    tank.install_block(col, mLengths, mUpShapes, mDownShapes)
                    result = (tank.t_id * 1000) + (col + 1) # 1부터 시작하는 인덱스이므로 +1
                    return result
    return 0

def pourIn(mWater: int) -> Result:
    rs_id, rs_h, rs_used = 0,0,0

    for tank in tank_list:
        # 탱크의 최대 수위
        max_h = 0
        # 탱크에 들어간 물의 양
        max_water = 0

        # 이진탐색을 이용한 최대수위 탐색
        top, bottom = tank.t_h, 1
        while bottom <= top:
            middle = (top + bottom) // 2
            need_waters = tank.need_waters[middle]

            if 0 < need_waters <= mWater:
                max_h = middle
                max_water = need_waters
                bottom = middle + 1
            else:
                # 공급된 물의 양 1일때 need_water값이 4라면 높이 처리를 안해야하므로
                if need_waters == 0 and middle < tank.t_h:
                    bottom = middle + 1
                else:
                    top = middle - 1

        #print(max_h,max_water)
        if max_h > rs_h:
            rs_id, rs_h, rs_used = tank.t_id, max_h, max_water
        elif max_h > 0 and max_h == rs_h and max_water > rs_used:
            rs_id, rs_used = tank.t_id, max_water

    ret = Result()
    ret.ID, ret.height, ret.used = rs_id, rs_h, rs_used
    return ret
