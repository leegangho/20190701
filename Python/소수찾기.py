
def solution(n):
    answer=0
    search_list=[]
    for i in range(2,n+1):
        search_list.append(i)

        check_list=[]


    for i in search_list:
        for j in range(1,i-1):
            if i % j==0:
                break    
        check_list.append(i)        

    return check_list

print(solution(10))