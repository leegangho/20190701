import heapq
def solution(stock,dates,supplies,k):
    answer=0
    index=0
    h=[] # heap 을 만듭니다. 

    while(stock < k): # stock가 k이면 
        # index=0 , len(dates)=3
        for i in range(index,len(dates)): # 0,1,2
            if dates[i] <= stock:
                heapq.heappush(h,(-supplies[i],supplies[i]))
                index=i+1
            else:
                break
        stock+=heapq.heappop(h)[1] #supplies[i]
        # heapq.heappush(h,(-supplies[i],supplies[i]))
        # 최대 힙구조로, 최대 값을 계속 pop
        answer=answer+1
    return answer

stock=4
dates=[4,10,15]
supplies=[20,5,10]

result=solution(4,dates,supplies,30)
print(result)