from collections import Counter

test=[["yello_hat","headgear"],["blue_suglasses","eyewear"],["green_turban","headgear"]]


def solution(test):
    category_count=Counter([category for i,category in test])
    answer=1
    for key in category_count:
        answer=answer*(category_count[key]+1)
    answer=answer-1
    return answer



# 경우의 수를 구하는 문제
# 각 종류별 의상의 개수를 구합니다.
# 종류별 의상의 개수를 전부 곱합니다.     -> 문제: 만약 5가지 종류가 있는데, 모자는 안쓰고, 나머지 의상을 입는 경우
# 의상의 개수+1 을 합니다.               -> 안입는 경우를 경우의 수로 추가합니다.
# 전부 곱한 후, 전체 값에서 -1 을 합니다. -> 조건: 최소 한개의 의상을 입는다. 전체에서 -1을 하는 경우는 전부 안입는 경우를 고려합니다. 
