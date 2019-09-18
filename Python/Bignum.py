def solution(numbers):
    
    numbers_str=list(map(str,numbers))
    #reverse=True 내림차순 정렬
    numbers_str.sort(key=lambda x: x*4,reverse=True)
    
    if numbers_str[0] == '0':
        return '0'
    else:
        answer=''.join(numbers_str)
        return answer

numbers=[4,4,4]
print(solution(numbers))
