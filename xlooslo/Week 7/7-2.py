def binarySearch(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, start, mid-1)
    else:
        return binarySearch(arr, target, mid+1, end)

n, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

result = binarySearch(arr, target, 0, n-1)
if result == None:
    print("원소 없다잉")
else:
    print(result + 1)