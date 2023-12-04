### https://adventofcode.com/2023/day/2


import numpy as np

CUBES_MAX_NUM = {
    "blue": 14, 
    "green": 13, 
    "red": 12
}


def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return filter(None, [line.strip() for line in f_in.readlines()])
    

    
def get_games_dict(data):
    games_dict = dict()    
    for line in data:
        game_id, game_sets = line.strip().split(':')
        game_id = game_id.replace('Game ', '').strip()
        game_sets = game_sets.strip().split(';')
        game_set_dict = dict()
        for game_set in game_sets:            
            game_set = game_set.strip().split(',')
            for item in game_set:
                num_cubes, cube_color = item.strip().split(' ')
                if not cube_color in game_set_dict:
                    game_set_dict[cube_color] = [int(num_cubes)]
                else:
                    game_set_dict[cube_color] += [int(num_cubes)]
        games_dict[game_id] = game_set_dict
    return games_dict


def is_valid_game_set(max_colors_dict):
    for color, max_value in max_colors_dict.items():
        if max_value > CUBES_MAX_NUM[color]:
            return False
    return True


def get_solution_1(data):
    valid_games = []
    for game_id, game_sets in data.items():
        max_colors = dict()
        for color, num_cubes_list in game_sets.items():
            if not num_cubes_list:
                num_cubes_list = [0]
            max_colors[color] = max(num_cubes_list)
        if is_valid_game_set(max_colors):
            valid_games.append(int(game_id))
    return sum(valid_games)
            
        
    
def get_solution_2(data):
    power_sum = 0
    for game_id, game_sets in data.items():
        max_colors = []
        for color, num_cubes_list in game_sets.items():
            if not num_cubes_list:
                num_cubes_list = [0]
            max_colors.append(max(num_cubes_list))
        power_sum += np.prod(max_colors)
    return power_sum
            



file = "data/day_2.txt"

data = get_games_dict(read_file(file))
solution_1 = get_solution_1(data)
solution_2 = get_solution_2(data)

print("Day 2 - Solution 1:", solution_1)
print("Day 2 - Solution 2:", solution_2)