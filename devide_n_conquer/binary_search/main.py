import sys
sys.stdin = open('sample_input.txt', 'r')


def binary_search(arr, target, last_path = None):
    l, r = 0, len(arr) - 1
    if l > r:
        return 0
    mid = (l+r) // 2

    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        if last_path == 'left':
            return 0
        return binary_search(arr[:mid], target, 'left')
    elif arr[mid] < target:
        if last_path == 'right':
            return 0
        return binary_search(arr[mid+1:], target, 'right')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # b에 속한 수가 a에 들어있으면서 탐색 과정에서 양쪽 구간을 번갈아 선택하게 되는 숫자의 개수
    a_arr = list(map(int, input().split()))
    a_arr.sort()
    b_arr = list(map(int, input().split()))

    total = 0
    for num in b_arr:
        total += binary_search(a_arr, num)

    print(f'#{tc} {total}')
