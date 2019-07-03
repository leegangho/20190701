
"""
# numbers를 파라미터로 갖는 함수
def solution(numbers):
    #numbers의 각 요소를 꺼내서 str으로 변환하고 다시 list에 넣는다.
    numbers=list(map(str,numbers))
    #확인용 출력 
    print(numbers)
    #문자로 바뀐 list를 정렬한다.
    #key를 통해서 정렬 기준을 주고, 내림차순으로 정렬
    numbers.sort(key=lambda x: x*3,reverse=True)
    #확인용 출력
    print(numbers)
    #리스트를 한번에 묶어서 반환
    return ''.join(numbers)

numbers=[6,10,2,3,30]

print(solution(numbers))
"""

def solution(numbers):
    
    numbers_str=list(map(str,numbers))
    #reverse=True 내림차순 정렬
    numbers_str.sort(key=lambda x: x*4,reverse=True)
    
    if numbers_str[0] == '0':
        return '0'
    else:
        answer=''.join(numbers_str)
        return answer

numbers=[6,10,2]
print(solution(numbers))
