from typing import List
from collections import defaultdict


# 평면의 길이
n = 0
# 해시값
# (해시값) = [ (좌표),.....]
hash_val = defaultdict(list)

hash_cnt_data = defaultdict(list)
# 누적합 배열
prefix_matrix = [[]]

# 고유 해시값 계산 변수
binary_val = [1]
for i in range(1,26):
    binary_val.append(binary_val[i-1]*2)

#print(binary_val)

def trans_to_hash(x,y,matrix):
    hash_list = []

    for k in range(4):
        idx = 0
        hash_n = 0
        for i in range(5):
            for j in range(5):
                if k == 0: # 정방향
                    r,s = i, j
                elif k == 1:  # 90도
                    r,s = 4-j, i
                elif k == 2: # 180도
                    r, s = 4-i, 4-j
                elif k == 3:  # 270도
                    r,s = j, 4-i
                #print(matrix[x+r][y+s])
                if matrix[x+r][y+s]:
                    hash_n += binary_val[idx]
                idx += 1
        hash_list.append(hash_n)
        #print(hash_list)

    return min(hash_list)


def init(N : int, mPlane : List[List[int]]) -> None:
    global n, hash_val, prefix_matrix
    n = N
    hash_val = defaultdict(list)
    hash_cnt_data = defaultdict(list)
    prefix_matrix = [ [0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix_matrix[i][j] = (
                mPlane[i-1][j-1] + prefix_matrix[i-1][j] + prefix_matrix[i][j-1] - prefix_matrix[i-1][j-1]
            )
    # print(prefix_matrix[1])
    # print(prefix_matrix[2])
    # print(prefix_matrix[3])
    # for item in prefix_matrix:
    #     print(item)
    visited = set()
    #print(N)
    for col in range(5,N):
        row = 5
        while row <= N:
            #print(row,col)
            st_col, st_row = col - 4, row - 4
            star_cnt = (
                prefix_matrix[row][col] + prefix_matrix[row-5][col-5]
                - prefix_matrix[row-5][col] - prefix_matrix[row][col-5]
            )
            if star_cnt != 7 or (st_row,st_col) in visited:
                row += 1
                continue
            # print(st_row,st_col, ':', N)
            hash_data = trans_to_hash(st_row-1, st_col-1, mPlane)

            for i in range(st_row, st_row+5):
                for j in range(st_col, st_col+5):
                    visited.add((i,j))
                    hash_val[hash_data].append((i-1, j-1))

            hash_cnt_data[hash_data].append((row,col))
            #print(hash_data)
            #print(hash_val)
            row += 5

    for key in hash_val:
        hash_val[key].sort()

def getCount(mPiece : List[List[int]]) -> int:
    hash_n = trans_to_hash(0,0,mPiece)
    #print(hash_n)
    result = len(hash_cnt_data[hash_n])
    #print(result)
    return result

def getPosition(mRow : int, mCol : int) -> int:

    return 0