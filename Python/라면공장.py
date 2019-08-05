import heapq

def solution(stock,dates,supplies,k):
    answer=0
    index=0
    h=[]
    while(stock < k):
        for i in range(index,len(dates)):
            if dates[i] <= stock:
                heapq.heappush(h,(-supplies[i],supplies[i]))
                index=i+1
            else:
                break
        stock+=heapq.heappop(h)[1]
        answer=answer+1
    return answer

"""
Python의 heapq 모듈!!! 
import heapq로 모듈을 불러옵니다.

heapq모듈에서는 파이썬의 리스트를 최소 힙처럼 다룰 수 있게 해줍니다.
heap=[]로 빈 리스트를 만들고, 추가 및 삭제한 리스트는 최소힙입니다. 

heap=[]
heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,7)
heapq.heappush(heap,3)
# [1,3,7,4]

heapq.heappop(heap) 를 하면 최소값을 삭제합니다. 
# 주의점 heap은 이진트리 배치형태이므로 반드시 두번째 작은값이, 두번째 index에 있다고 보장할 수 없다.
따라서 heappop()을 통해서 가장 작은 원소를 삭제 후, heap[0]으로 접근합니다. 

# 기존 리스트를 heap으로 변환하기!  # heapify() 함수를 사용합니다. 
heap=[4,1,7,3,8,5]
heapq.heapify(heap) -> [1,3,5,4,8,7] 


# Python은 최소힙(Min Heap)입니다. 
# 응용해서 최대힙(Max Heap)을 만들어 봅니다. 

import heapq

nums=[4,1,7,3,8,5]
heap=[]

for num in nums:
    heapq.heappush(heap,(-num,num))

while heap:
    print(heapq.heappop(heap)[1])

# heap sort 힙 정렬!
import heapq

def heap_sort(nums):
    heap=[]
    for num in nums:
        heapq.heappush(heap,num)
    sorted_nums=[]
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

"""