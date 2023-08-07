def solution(numbers:list, hand):
    numbers = [str(i) for i in numbers]
    answer = ''
    coordinate_dict = {
        '1':[0, 0], '2':[0, 1], '3':[0, 2],
        '4':[1, 0], '5':[1, 1], '6':[1, 2],
        '7':[2, 0], '8':[2, 1], '9':[2, 2],
        '*':[3, 0], '0':[3, 1], '#':[3, 2]
    }
    position = {}
    default_left = ['1', '4', '7']
    default_right = ['3', '6', '9']
    position = {'L':coordinate_dict["*"], 'R':coordinate_dict['#']}
    if hand == 'right':
        for num in numbers:
            if num in default_left:
                answer += 'L'
                position['L'] = coordinate_dict[num]
            elif num in default_right:
                answer += 'R'
                position['R'] = coordinate_dict[num]
            else:
                if (abs(coordinate_dict[num][0]-position['L'][0]) + abs(coordinate_dict[num][1]-position['L'][1]) 
                  < abs(coordinate_dict[num][0]-position['R'][0]) + abs(coordinate_dict[num][1]-position['R'][1])):
                    answer += 'L'
                    position['L'] = coordinate_dict[num]
                else:
                    answer += 'R'
                    position['R'] = coordinate_dict[num]
        return answer
    for num in numbers:
        if num in default_left:
            answer += 'L'
            position['L'] = coordinate_dict[num]
        elif num in default_right:
            answer += 'R'
            position['R'] = coordinate_dict[num]
        else:
            if (abs(coordinate_dict[num][0]-position['L'][0]) + abs(coordinate_dict[num][1]-position['L'][1]) 
                > abs(coordinate_dict[num][0]-position['R'][0]) + abs(coordinate_dict[num][1]-position['R'][1])):
                answer += 'R'
                position['R'] = coordinate_dict[num]
            else:
                answer += 'L'
                position['L'] = coordinate_dict[num]
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = "right"
print(solution(numbers, hand))
# LRLLLRLLRRL
# LRLLRRLLLRR
# LLRLLRLLRL