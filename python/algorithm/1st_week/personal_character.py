def solution(survey:str, choices):
    answer = ''
    type = ["RT", "FC", "MJ", "AN"]
    type_dict = {}
    for i in type:
        type_dict.setdefault(i, 0)
    for i in range(len(survey)):
        reversed_survey_v = "".join(reversed(survey[i]))
        if reversed_survey_v in type:
            type_dict[reversed_survey_v] -= (choices[i]-4)
            continue
        type_dict[survey[i]] += (choices[i]-4)
    for k, v in type_dict.items():
        if v < 0:
            answer += k[0]
        elif v > 0:
            answer += k[1]
        else:
            answer += sorted(list(k))[0]
    print(type_dict)
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
solution(survey, choices)
# survey = ["TR", "RT", "TR"]
# choices = [7, 1, 3]

# print(solution(survey, choices))