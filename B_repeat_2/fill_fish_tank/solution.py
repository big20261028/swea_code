from typing import List

class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0


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
