from typing import List

class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0

class Fish_tank:
    def __init__(self,mID,width,height,lengths,up_shapes) -> None:
        self.mID = mID
        self.tank_width = width
        self.tank_height = height
        self.lengths = list(lengths)
        self.up_shapes = list(up_shapes)
        self.need_waters = [0] * (height+1)
        self.cal_water()
        self.subset_joint = {}
        self.find_subset_joint()


    # 어항에 특정 물 높이 달성에 필요한 물의 양 구하기
    def cal_water(self):
        # 계산하기 편하게 tank_height + 1
        h_index = [0] * (self.tank_height + 1)
        for height in self.lengths:
            if height <= self.tank_height:
                h_index[height] += 1

        # 물이 채워지는 칸 수
        can_fill_idx_cnt = 0
        # 채워진 물의 양
        total_water = 0
        for h in range(1,self.tank_height + 1):
            can_fill_idx_cnt += h_index[h-1]
            total_water += can_fill_idx_cnt
            self.need_waters[h] = total_water

    # 3개씩 연속되는 연결부 데이터 만들기
    def find_subset_joint(self):
        self.subset_joint.clear()

        for i in range(self.tank_width - 2):
            joint_set = (self.up_shapes[i],self.up_shapes[i+1],self.up_shapes[i+2])
            if joint_set not in self.subset_joint:
                self.subset_joint[joint_set] = []
            self.subset_joint[joint_set].append(i)

    # 블록을 설치할 수 있는지 확인
    def can_install_block(self,column,block_h):
        a = self.lengths[column] + block_h[0]
        b = self.lengths[column+1] + block_h[1]
        c = self.lengths[column+2] + block_h[2]

        # 블록 설치 후 높이가 탱크보다 크면 안됨
        if a > self.tank_height or b > self.tank_height or c > self.tank_height:
            return False

        # 설치한 블록의 높이와 설치 전 블록의 높이가 같으면 안됨
        if max(self.lengths[column],self.lengths[column+1]) >= min(a,b):
            return False
        if max(self.lengths[column+1],self.lengths[column+2]) >= min(b,c):
            return False

        return True

    # 블록 설치하기
    def install_block(self,column,block_h,block_u):
        for i in range(3):
            self.lengths[column+i] += block_h[i]
            self.up_shapes[column+i] = block_u[i]
        # 변경된 블록 높이와 상부 조인트에 맞춰 다시 계산하기
        self.find_subset_joint()
        self.cal_water()

tanks_list = []

def init(
        N: int,
        mWidth: int,
        mHeight: int,
        mIDs: List[int],
        mLengths: List[List[int]],
        mUpShapes: List[List[int]]) -> None:
        global  tanks_list
        temp = []
        for i in range(N):
            temp.append(Fish_tank(mIDs[i],mWidth,mHeight,mLengths[i],mUpShapes[i]))
        temp.sort(key=lambda x:x.mID)
        tanks_list = temp

def checkStructures(
        mLengths: List[int],
        mUpShapes: List[int],
        mDownShapes: List[int]) -> int:
    down_joints = (mDownShapes[0],mDownShapes[1],mDownShapes[2])
    cnt = 0
    for tank in tanks_list:
        if down_joints in tank.subset_joint:
            for col in tank.subset_joint[down_joints]:
                if tank.can_install_block(col,mLengths):
                    cnt += 1
    return cnt

def addStructures(mLengths: List[int],
                  mUpShapes: List[int],
                  mDownShapes: List[int]) -> int:
    down_joints = (mDownShapes[0], mDownShapes[1], mDownShapes[2])
    for tank in tanks_list:
        if down_joints in tank.subset_joint:
            for col in tank.subset_joint[down_joints]:
                if tank.can_install_block(col,mLengths):
                    result = (tank.mID * 1000) + (col + 1)
                    tank.install_block(col,mLengths,mUpShapes)
                    return result
    return 0

def pourIn(mWater: int) -> Result:
    result_id, result_h, result_used = 0,0,0

    for tank in tanks_list:
        bottom, top = 1, tank.tank_height
        water_h, water_used = 0,0
        while bottom <= top:
            mid = (bottom+top) // 2
            need = tank.need_waters[mid]
            if 0 < need <= mWater:
                water_h, water_used = mid, need
                bottom = mid + 1
            else:
                if need == 0 and mid < tank.tank_height:
                    bottom = mid + 1
                else:
                    top = mid - 1

        # 높이가 높으면 바꾸기
        if water_h > result_h:
            result_id, result_h, result_used = tank.mID, water_h,water_used
        # 높이가 같으면 사용량 비교
        elif water_h > 0 and water_h == result_h:
            if water_used > result_used:
                result_id, result_used = tank.mID, water_used

    ret = Result()
    ret.ID, ret.height, ret.used = result_id, result_h, result_used
    return ret
