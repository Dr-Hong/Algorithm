# 이진 탐색 소스코드 구현 (재귀함수)

def binarySearch(array, target, start, end){
    if (start > end)
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        binarySearch(array, target, start, mid-1)
    else:
        binarySearch(array, target, mid+1, end)
}

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binarySearch(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)