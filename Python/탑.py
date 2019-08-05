heights=[6,9,5,7,4]
#a=len(heights)
#print(a)
#start=heights.pop()
#end=heights.pop()
#b=len(heights)
#print(b)
#result=[]
#index=len(heights)


# case 1 

def solution(heights):
    answer=[]
    length=len(heights)  # length=5
    for i in range(length): # i: 0~4 , 총 5번 실행 
        start=heights.pop()  # heights에서 4,7,5,9,6 순서대로 꺼냅니다.
        length2=len(heights) # lengths2 는 4,3,2,1...
        
        for j in range(length2): # j:0~3, 총 4번 실행
            if start < heights[length2-j-1]:
                answer.append(length2-j)
                break
            else:
                if j==(length2-1):
                    answer.append(0)
                continue
    answer.append(0) 
    answer.reverse()      
    return answer
