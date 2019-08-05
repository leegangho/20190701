#test=[12,10,13,9,5,4]
#print(sorted(test))

def solution(scoville,K):
    answer=0
    sort_list=sorted(scoville)
    while True:
        answer+=1
        one=sort_list.pop(0)
        two=sort_list.pop(0)
        result=one+(two*2)
        if K > result:
            sort_list.append(result)
            sort_list=sorted(sort_list)
        else:
            break
    return answer

test=[1,2,3,9,10,12]
K=7
result=solution(test,K)
print(result)