def solution(participant,completion):
    p_set=set(participant)
    c_set=set(completion)
    a=list(p_set-c_set)
    for i in a:
        answer=i
    return answer
