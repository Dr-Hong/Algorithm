# 퀵 정렬 소스 코드

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end: return # 원소가 1개인 경우 종료
    pivot = start; # 첫 번째 피봇은 start로 잡는다.
    left = start + 1
    right = end

    while left <= right :
        while left <= end and array[left] <= array[pivot]:
            left += 1 # 피봇보다 큰 데이터를 찾을 때 까지 반복
        while right >= start and array[right] >= array[pivot]:
            right -= 1 # 피봇보다 작은 데이터를 찾을 때 까지 반복
        if left < right: # 엇갈렸다면 둘 교체
            array[right], array[pivot] = array[right], array[pivot]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left] , array[right] = array[right] , array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right - 1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array) - 1)
print(array)