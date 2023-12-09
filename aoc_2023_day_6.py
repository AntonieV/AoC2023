### https://adventofcode.com/2023/day/6

import re
import numpy as np

def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return list(filter(None, [line.strip() for line in f_in.readlines()]))
    

def get_value(data_row, title, type_str=""):
    data_row = data_row.replace(title, "").strip()
    if type_str == "int":
        return [int(item) for item in re.split(r'\s+', data_row)]
    return [item for item in re.split(r'\s+', data_row)]
    
    
def parse_input_part_1(data):
    _time = get_value(data[0], "Time:", "int")
    dist = get_value(data[1], "Distance:", "int")
    return list(zip(_time, dist))


def parse_input_part_2(data):
    _time = get_value(data[0], "Time:")
    dist = get_value(data[1], "Distance:")
    return int(''.join(_time)), int(''.join(dist))

    
def get_solution_1(time_dist_tuples):
    win_solutions = []    
    for time, dist in time_dist_tuples:
        solution_count = 0
        for min_time in range(time):
            if dist < (time - min_time) * min_time:
                solution_count += 1
            if solution_count > 0 and dist > (time - min_time) * min_time:
                break
        win_solutions.append(solution_count)
    return np.prod(win_solutions)
                    
    
def get_solution_2(time, dist):
    solution_count = 0
    for min_time in range(time):
        if dist < (time - min_time) * min_time:
            solution_count += 1
        if solution_count > 0 and dist > (time - min_time) * min_time:
            break
    return solution_count


file = "data/day_6.txt"
# file = "data/day_6_test.txt"

time_dist_pairs = parse_input_part_1(read_file(file))
solution_1 = get_solution_1(time_dist_pairs)

time, dist = parse_input_part_2(read_file(file))
solution_2 = get_solution_2(time, dist)

print("Day 6 - Solution 1:", solution_1)  # 6209190
print("Day 6 - Solution 2:", solution_2)  # 28545089