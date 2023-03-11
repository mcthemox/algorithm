#1920

# 나의풀이
import sys
input = sys.stdin.readline

a = int(input())
a_list = set(map(int,input().split()))
b = int(input())
b_list = list(map(int,input().split()))

for i in b_list:
    if i in a_list:
        print(1)
    else:
        print(0)
# 둘 다 list에 넣으면 시간초과
# set() 은 순서가 없기 때문에 시간단축이 된다.

# 이분탐색 풀이
import sys
input = sys.stdin.readline

a = int(input())
a_list = list(map(int, input().split()))
b = int(input())
b_list = list(map(int, input().split()))
a_list.sort()    # 리스트 정렬

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2

    while start <= end:
        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in range(b):
    print(binary_search(a_list, b_list[i]))