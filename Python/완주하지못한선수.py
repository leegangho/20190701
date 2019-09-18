def solution(participant,completion):
    p_set=set(participant)
    c_set=set(completion)
    a=list(p_set-c_set)
    for i in a:
        answer=i
    return answer

# set() 설명
# 중복을 허용하지 않습니다.
# 순서가 없습니다. 

# 다른 사람 풀이 

import collections

def solution2(participant,completion):
    answer=collections.Counter(participant)-collections.Counter(completion)
    return list(answer.keys())[0]

participant=["mislav", "stanko", "mislav", "ana"]	
completion=["stanko", "ana", "mislav"]

print(solution2(participant,completion))
print(solution(participant,completion))