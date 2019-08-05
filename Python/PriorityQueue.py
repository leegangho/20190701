# 큐를 임포트 합니다. 
from queue import PriorityQueue

# 비어있는 우선순위 큐를 만듭니다. (초기화)
que=PriorityQueue()

# 기본값은 무한대입니다. 
# 사이즈가 있는 queue를 만들고 싶으면 maxsize= 로 크기를 지정합니다. 
que=PriorityQueue(maxsize=8)

# put() 메서드를 이용해서 우선순위 큐에 원소를 추가합니다. 
que.put(4)
que.put(1)
que.put(7)
que.put(3)

que.get() # 1
que.get() # 3
que.get() # 4
que.get() # 7

# 정렬 기준 변경 
# 오름차순이 아닌, 다른 기준으로 원소가 정렬되기를 원한다면, (우선순위, 값)의 튜플형태로 
# 데이터를 추가하고 삭제합니다. 

que.put((3,'Apple'))
que.put((1,'Banana'))
que.put((2,'Cherry'))

print(que.get()[1]) # Banana
print(que.get()[1]) # Cherry
print(que.get()[1]) # Apple 


