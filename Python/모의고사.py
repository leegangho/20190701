
from itertools import cycle 

def solution (answer):
    answer=[]
    yes_answer=[]
    pattern_supo_1=[1,2,3,4,5]
    pattern_supo_2=[2,1,2,3,2,4,2,5]
    pattern_supo_3=[3,3,1,1,2,2,4,4,5,5]
    score_supo=[0,0,0]

    for supo_1,supo_2,supo_3,answer in list(zip(cycle(pattern_supo_1),cycle(pattern_supo_2),cycle(pattern_supo_3),answer)):
        
        if supo_1==answer:
            #pattern_supo_1
            score_supo[0]+=1
       
        if supo_2==answer:
            #pattern_supo_2
            score_supo[1]+=1
       
        if supo_3==answer:
            #pattern_supo_3
            score_supo[2]+=1
        

    print(score_supo)     
    for i,score in enumerate(score_supo):
        if score == max(score_supo):
            yes_answer.append(i+1)
    #print(yes_answer)
    return yes_answer
    
answer=[1,2,3,4,5]
x = solution(answer)

print(x)
#list(zip(cycle(pattern_supo_1),cycle(pattern_supo_2),cycle(pattern_supo_3),answer))
