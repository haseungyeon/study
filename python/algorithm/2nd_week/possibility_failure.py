def solution(N, stages):
    answer = []
    total_players = len(stages)
    for i in range(1, N+1):
        players_on_stage = stages.count(i)        
        if total_players == 0:
            failure_rate = 0
        else:
            failure_rate = players_on_stage / total_players
        answer.append((i, failure_rate))
        total_players -= players_on_stage
    answer = [stage for stage, _ in sorted(answer, key=lambda x: x[1], reverse=True)]
    return answer