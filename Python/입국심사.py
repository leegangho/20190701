"""
1. 심사관 = 입국자 이면 한번에 끝-> times의 가장 긴 시간을 return
2. 심사관 > 입국자 이면 times의 최소값부터 배치하고, 더하고 return.
3. 심사관 < 입국자 이면 이분 탐색을 실시
"""

def solution(n,times):
    answer=0
    #심사관 수
    times_human=len(times)
    times.sort(reverse=False)

    if n==times_human:#심사관과 입국자가 같은경우
        answer=max(times)

    elif n < times_human: #심사관이 더 많은 경우
        answer=sum(times[:n])

    else: #입국자가 더 많은 경우
        Low=1
        High=n*max(times)
        
        while Low+1<High:
            total=0
            Mid=(Low + High)//2

            # Mid라는 시간은 몇명일때 최소로 걸리는 시간인가?    
            for i in times:
                total+=Mid//i
            
            if total >= n:
                High=Mid
            else:
                Low=Mid
        return High
    return answer

times=[7,10]
x=solution(1,times)
print(x)