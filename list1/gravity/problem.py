import sys
sys.stdin = open("in.txt", "r")

'''
각 상자별로 낙차가 가장 큰 값 확인
그 중, 가장 큰 값 출력


'''

T = int(input())
for test_case in range(1, T + 1):
    # 방의 길이
    N = int(input())
    # 인덱스별 상자 개수
    arr = list(map(int, input().split()))
    #print(arr)

    max_fall = 0
    for idx1,item1 in enumerate(arr):
       #print(f'targe: {item1}')
        cnt = 0
        for idx2,item2 in enumerate(arr[idx1+1:]):
            if item2 < item1:
                cnt += 1
        # target_fall = N - cnt - (idx1 + 1)
        if cnt > max_fall:
            #print("최댓값 변화:",cnt)
            max_fall = cnt

    result = None
    print(f"#{test_case} {max_fall}")
