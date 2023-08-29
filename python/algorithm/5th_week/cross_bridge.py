from collections import Counter, deque
from copy import deepcopy
def solution(bridge_length, weight, truck_weights):
    counter = Counter(truck_weights)
    print(counter)
    print(dict(sorted(counter.items(), reverse=True)))
    sorted_truck = dict(sorted(counter.items(), reverse=True))
    answer = 0
    cur_bridge = deque(maxlen=bridge_length)
    before_bridge = []
    while sorted_truck:
        if before_bridge == cur_bridge:
            cur_bridge.popleft()
        cur_bridge_weight = sum(cur_bridge)
        before_bridge = deepcopy(cur_bridge)
        for truck_weight in sorted_truck:
            if weight-cur_bridge_weight >= cur_bridge_weight:
                cur_bridge.append(truck_weight)
                sorted_truck[truck_weight] -= 1
                answer += 1
                if sorted_truck[truck_weight] == 0:
                    sorted_truck.pop(truck_weight, None)
                break

            
            # if left_truck_cnt == 0:
            #     sorted_truck.pop(truck_weight, None)
            # if weight%truck_weight == 0 and (weight / truck_weight) <= bridge_length:
            #     if left_truck_cnt >= (weight / truck_weight):
            #         sorted_truck[truck_weight] -= (weight / truck_weight)
            #         answer += (weight / truck_weight)
            #     else:
            #         sorted_truck.pop(truck_weight, None)
            #         answer += left_truck_cnt
            # elif 
            #     cur_bridge_weight += truck_weight 
                
            
        # print(truck_weight)
                
        # pass
    
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))