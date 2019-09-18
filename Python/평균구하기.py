def solution(arr):
    answer=0
    result=sum(arr)
    N=len(arr)
    answer=result/N
    return answer


a=[1,2,3,4]
test=solution(a)
print(test)
