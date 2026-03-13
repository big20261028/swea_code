from typing import List
from collections import defaultdict

# 평면 크기
plane_n = 0
# 해시 별 좌표
# 해시값 : [ (대표좌표), (대표좌표), .... ]
hash_pos = defaultdict(list)
# 좌표 별 해시값
# (좌표) = 해시값
pos_hash = {}
# 누적합 이중리스트
prefix_matrix = [[]]


def tran_to_hash(x, y, matrix):
    candidate_hashes = []

    #print('시작좌표', x, y)
    for k in range(4):
        hash_val = 0
        val = 1
        for i in range(5):
            for j in range(5):
                if k == 0:
                    r,s = i,j
                elif k == 1:
                    r,s = 4-j, i
                elif k == 2:
                    r,s = 4-i, 4-j
                elif k == 3:
                    r,s = j, 4-i

                if matrix[x+r][y+s]: # 1일경우 유효
                    # print(matrix[x+r][y+s])
                    # print(val)
                    hash_val += val
                #print(val)
                val *= 2
        
        candidate_hashes.append(hash_val)
    #     print('해쉬 1개 완성:', hash_val)
    # print(candidate_hashes)
    return min(candidate_hashes)


def init(N : int, mPlane : List[List[int]]) -> None:
    global plane_n, hash_pos, pos_hash, prefix_matrix

    plane_n = N
    hash_pos = defaultdict(list)
    pos_hash.clear()
    prefix_matrix = [ [0] * (N+1) for _ in range(N+1) ]

    for i in range(1,N+1):
        for j in range(1,N+1):
            prefix_matrix[i][j] = (
                prefix_matrix[i-1][j] + prefix_matrix[i][j-1] - prefix_matrix[i-1][j-1] + mPlane[i-1][j-1]
            )

    for row in range(5,N+1):
        col = 5
        while col < (N+1):
            st_row, st_col = row-5, col-5
            star_count = (
                prefix_matrix[row][col] - prefix_matrix[row-5][col] - prefix_matrix[row][col-5]
                + prefix_matrix[row-5][col-5]
            )
            if star_count != 7 or (st_row,st_col) in pos_hash:
                col += 1
                continue

            #print(star_count, (st_row, st_col))

            hash_val = tran_to_hash(st_row, st_col, mPlane)
            hash_pos[hash_val].append((st_row,st_col))

            for i in range(st_row, st_row + 5):
                for j in range(st_col, st_col + 5):
                    pos_hash[(i,j)] = hash_val

            col += 5

    #print(hash_pos)
    #print(pos_hash)

    for key in hash_pos:
        hash_pos[key].sort()


def getCount(mPiece : List[List[int]]) -> int:
    target_hash = tran_to_hash(0,0,mPiece)
    result = len(hash_pos[target_hash])
    #print(result)
    return result

def getPosition(mRow : int, mCol : int) -> int:
    target_hash = pos_hash[(mRow,mCol)]
    (st_row, st_col) = hash_pos[target_hash][0]
    row, col = st_row + 2, st_col + 2
    result = (row * 10000) + col
    #print(target_hash)
    return result