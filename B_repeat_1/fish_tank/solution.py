from typing import List

from collections import defaultdict


class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0

class FishTank:
    def __init__(self, id, width, height, block_height, up_shape):
        self.id = id
        self.width = width
        self.height = height
        self.block_height = list(block_height)
        self.up_shape = list(up_shape)
        self.upper_subset = {}
        self.cal_upper_subset()
        self.require_water_info = [0] * height

    def cal_upper_subset(self):
        temp_dict = defaultdict(list)
        for i in range(self.width - 2):
            upper_set = [self.up_shape[i],self.up_shape[i+1],self.up_shape[i+2]]
            temp_dict[upper_set].append(i)
        self.upper_subset = temp_dict

    def cal_water_need(self):
        fill_idx = [0] * (self.height + 1)
        for h in self.block_height:
            fill_idx[h] += 1

        water_fill_rank = 0
        total = 0
        for h in range(self.height+1):
            water_fill_rank += fill_idx[h]
            total += water_fill_rank
            self.require_water_info[h+1] = total # 테스트 해보고 바꾸기

    def can_install_check(self,col,blocks):
        ist_block_1 = self.block_height[col] + blocks[0]
        ist_block_2 = self.block_height[col+1] + blocks[1]
        ist_block_3 = self.block_height[col+2] + blocks[2]








def init(N: int, mWidth: int, mHeight: int, mIDs: List[int], mLengths: List[List[int]], mUpShapes: List[List[int]]) -> None:
        pass

def checkStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:
    return 0

def addStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:
    return 0

def pourIn(mWater: int) -> Result:
    ret = Result()
    ret.ID = ret.height = ret.used = 0
    return ret
