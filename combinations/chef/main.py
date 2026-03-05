import sys
sys.stdin = open('sample_input.txt','r')

from itertools import combinations
from itertools import permutations

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    ingredients = [ i for i in range(N) ]

    min_val = float('inf')

    a_coms = combinations(ingredients,N//2)

    for a_com in a_coms:
        b_com = [ item for item in ingredients if item not in a_com ]

        a_pos_list = permutations(a_com,2)
        b_pos_list = permutations(b_com,2)

        a_combo = 0
        b_combo = 0
        for ax,ay in a_pos_list:
            a_combo += matrix[ax][ay]

        for bx,by in b_pos_list:
            b_combo += matrix[bx][by]

        diff = abs(a_combo-b_combo)
        min_val = min(min_val,diff)

    print(f'#{tc} {min_val}')