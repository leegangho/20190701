def solution(n,lost,reserve):
    LOST=len(lost)
    RESERVE=len(reserve)
    answer = (n-LOST)
    for i in range(0,RESERVE):
        element = reserve[i]
        plus = element + 1
        minus = element - 1
        for j in range(0,LOST):
            if lost[j] == plus | lost[j] == minus:
                answer+=1
                j=j+1
    return answer


def solution2(n,lost,reserve):
    set_reserve=set(reserve)-set(lost)
    set_lost=set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)



n=5
lost=[3]
reserve=[1]
result=solution2(n,lost,reserve)
print(result)

# n에서 lost의 개수를 빼기 len(lost)
# reserve의 각 원소들에서 +-1 을 하여 lost의 원소값이 있다면 answer+=1
