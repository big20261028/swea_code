import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque

def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(deque(left_half), deque(right_half))


def merge(left, right):
    global cnt

    if left and right:
        if left[-1] > right[-1]:
            cnt += 1

    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())

    result.extend(left)
    result.extend(right)

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    result = merge_sort(arr)

    print(f'#{tc} {result[N//2]} {cnt}')