def solution(brown,red):
    for a in range(1,int(red**0.5)+1):
        if not red % a:
            b=red//a
            if 2*a+2*b+4==brown:
                return [b+2,a+2]
