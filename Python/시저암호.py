def solution(s,n):
    result=[]
    for i in range(0,len(s)):
        test=ord(s[i])
        if test >=65 and test <= 90:
            test += n 
            if test >= 90:
                test = 65
                test += (n-1)
            result.append(chr(test))
        elif test >= 97 and test <= 122:
            test += n
            if test >= 122:
                test = 97
                test += (n-1)
            result.append(chr(test))
    return "".join(result)

s="AB"
n=1
result=solution(s,n)

print(result[0])

def solution(s,n):
    answer=''
    s1=list(s)
    k=ord('z')-ord('a')+1
    n %= k
    for i in s1:
        if i is ' ':
            answer+=' '
        if i.isupper():
            if (ord(i)+n) > ord('Z'):
                answer += chr(ord(i)+n-k)
            else:
                answer += chr(ord(i)+n)
        elif i.islower():
            if (ord(i)+n) > ord('z'):
                answer += chr(ord(i)+n-k)
            else:
                answer += chr(ord(i)+n)
    return answer


"""
65~90, 97~122
s: "AB" -> "BC" ,n=1
s: "z" -> "a" , n=1
s: "aBz" -> "eFd", n=4
"""

#  a~z 까지 리스트를 만듭니다.
#  입력받은 s를 a~z형태로 변환 isupper()
#  n의 값만큼 리스트에서 오른쪽으로 움직입니다.
#  