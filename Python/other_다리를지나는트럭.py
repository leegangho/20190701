import collections 
DUMMY_TRUCK=0

class Bridge(object):
    def __init__(self,length,weight):
        self._max_length=length
        self._max_weight=weight
        self._queue=collections.deque()
        self._current_weight=0

    def push(self,truck):
        next_weight=self._current_weight+truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight=next_weight
            return True
        else:
            False
    
    def pop(self):
        item=self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight,self._max_weight,list(self._queue))

def solution(bridge_length,weight,truck_weight):
    # Bridge 클래스를 사용해서 객체를 만들어냅니다. 
    # Bridge 클래스는 pop, push의 메서드 (기능)을 가지고 있습니다.
    bridge=Bridge(bridge_length,weight)

    # 트럭을 deque의 배열로 만들어 둡니다. 
    # 건너야할 트럭의 개수만큼! 
    trucks=collections.deque(w for w in truck_weight)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)
    # 또한 다리 길이 만큼 만들어 둡니다. 


    # 최소 시간 카운트 시작! 
    count=0
    while trucks:
        bridge.pop()
        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)
        count += 1
    while bridge:
        bridge.pop()
        count += 1 
    return count

def main():
    print(solution(2,10,[7,4,5,6]),8)
    print(solution(100,100[10]),101)
    print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]),110)

#if __name__ == '__main__':
#    main()


