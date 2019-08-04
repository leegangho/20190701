priorities=[2,1,3,2]

def solution(priorities,location):
    answer=0
    max_value=max(priorities)
    while True:
        A=priorities.pop(0)
        if max_value==A :
            answer+=1
            if location==0:
                break
            else:
                location-=1
            max_value=max(priorities)  
        else:
            priorities.append(A)
            if location==0:
                location=len(priorities)-1
            else:
                location-=1
    return answer

result=solution(priorities,2)
print(result)
"""
# 다른 사람 풀이
def solution2(p,l):
    ans=0
    m=max(p)
    while True:
        v=p.pop(0)
        if m==v:
            ans+=1
            if l==0:
                break
            else:
                l-=1
            m=max(p)
        else:
            p.append(v)
            if l==0:
                l=len(p)-1
            else:
                l-=1
    return ans


result=solution2(priorities,2)
print(result)
"""