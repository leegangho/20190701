def solution(answer):
    p=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    s=[0]*len(p)

    for q,a in enumerate(answer):
        for i,v in enumerate(p):
            if a== v[q % len(v)]:
                s[i] += 1
    return [i+1 for i,v in enumerate(s) if v==max(s)]


# operator, itertools, functools 모듈을 사용하면 좀더 편리 할 수 있다.
