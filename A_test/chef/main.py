import sys
sys.stdin = open('sample_input.txt','r')

from itertools import combinations
from itertools import permutations

T = int(input())
for tc in range(1,T+1):
    # N: 식재료 개수
    # N은 반드시 짝수/ 각 식재료를 다 쓸 필요는 없다.
    # 하지만, 식재료 2가지를 선택해야만 시너지가 발생한다.

    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    ingredients = { i for i in range(N) }
    # # N개의 재료 중 N/2개를 선택하는 조합 구하기
    items = combinations(ingredients,N//2)

    min_val = float('inf')

    for A in items:
        A = set(A)
        B = ingredients.difference(A)
        A_pos = list(permutations(A, 2))
        B_pos = list(permutations(B, 2))
        A_sum = 0
        for i,j in A_pos:
            A_sum += matrix[i][j]
        B_sum = 0
        for i,j in B_pos:
            B_sum += matrix[i][j]

        total = abs(A_sum - B_sum)
        min_val = min(total,min_val)

    print(f'#{tc} {min_val}')




    #     print(target)
    # print('-')




    # print('-')
    # # 조합들의 각 좌표 구하기
    # for item in food_items:
    #     pos_datas = list(permutations(item,2))
    #     print(pos_datas)
    #     print('#')
