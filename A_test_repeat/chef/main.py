import sys
sys.stdin = open('sample_input.txt','r')

from itertools import combinations
from itertools import permutations

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    target = [ i for i in range(N) ]

    min_val = float('inf')

    com_a = list(combinations(target,N//2))
    #print(com_a)
    for item in com_a:
        # item = 첫 음식에서 사용할 재료 인덱스
        remains = [ idx for idx in target if idx not in item ]

        # item과 remains의 permutations 구하기
        # 나온 값을 모두 더하기
        a_target = permutations(item,2)
        b_target = permutations(remains,2)

        a_power = 0
        for x,y in a_target:
            a_power += matrix[x][y]
        b_power = 0
        for x2,y2 in b_target:
            b_power += matrix[x2][y2]

        diff = abs(a_power - b_power)
        min_val = min(min_val,diff)

    print(f'#{tc} {min_val}')