### https://adventofcode.com/2023/day/3


import re
import numpy as np



def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return [line.strip() for line in f_in.readlines() if line.strip()]
    

def is_symbol(char):
    return not bool(re.match(r"[A-Za-z0-9.]+", char))


def has_adjacent_symbol(matrix, i_row, i_col, num_rows, num_cols, current_number):    
    left = is_symbol(matrix[i_row, i_col - 1]) if i_col > 0 else False
    right = is_symbol(matrix[i_row, i_col + 1]) if i_col < num_cols - 1 else False
    top, bottom = False, False
    start = i_col - 1 if i_col > 0 else 0
    end = i_col + 2 if i_col < num_cols else num_cols - 1
    if i_row > 0:        
        top_region = matrix[i_row - 1, start : end]
        top = any([is_symbol(item) for item in top_region])
    if i_row < num_rows - 1:
        bottom_region = matrix[i_row + 1, start : end]
        bottom = any([is_symbol(item) for item in bottom_region])
    return any([left, right, top, bottom])
    

def get_solution_1(data):
    part_numbers = []
    matrix = np.array([list(line) for line in data])
    num_rows, num_cols = matrix.shape
    for idx_row, row in enumerate(matrix):
        current_number = ""
        is_adjacent_to_symbol = False
        for idx_col, cell_item in enumerate(row):
            if cell_item.isnumeric():
                current_number += cell_item 
                if not is_adjacent_to_symbol:
                    is_adjacent_to_symbol = has_adjacent_symbol(matrix, idx_row, idx_col, num_rows, num_cols, current_number)
                if idx_col < num_cols - 1 and not matrix[idx_row, idx_col + 1].isnumeric() or \
                idx_col == num_cols - 1:
                    if is_adjacent_to_symbol:
                        part_numbers.append(int(current_number))
                    current_number = ""
                    is_adjacent_to_symbol = False
    return sum(part_numbers)


def get_digits_by_side_shift(row, idx, num_cols, shift):
    number = ""
    while row[idx].isnumeric():
        number += row[idx]
        idx += shift
        if idx < 0 or idx == num_cols:
            number = number[::-1] if shift == -1 else number
            return number
    number = number[::-1] if shift == -1 else number
    return number


def get_number(row, current_idx, num_cols):
    current_val = row[current_idx]
    if current_val.isnumeric():
        return int(get_digits_by_side_shift(row, current_idx - 1, num_cols, shift=-1) + 
                   current_val + 
                   get_digits_by_side_shift(row, current_idx + 1, num_cols, shift=1))
    return None


def get_gear_region_value(row, region, start, end, num_cols):
    check_multi_region = list(filter(None, re.split(r"\D+", ''.join(region))))
    if len(check_multi_region) == 2:
        i_1 = start
        i_2 = end - 1
        res_1 = get_number(row, i_1, num_cols)
        res_2 = get_number(row, i_2, num_cols)
        if res_1 and res_2:            
            return [res_1, res_2]
        return [None]

    for i, char in enumerate(region):        
        if char.isnumeric():
            return [get_number(row, start + i, num_cols)]
    return [None]


def contains_digits(region):
    return bool(re.match(r"\D*\d+\D*", ''.join(region)))


def get_adjacent_numbers(matrix, i_row, i_col, num_rows, num_cols):
    items = []
    # left
    items += [get_number(matrix[i_row], i_col - 1, num_cols)] if i_col > 0 else [None]
    # right
    items += [get_number(matrix[i_row], i_col + 1, num_cols)] if i_col < num_cols - 1 else [None]
    top, bottom = None, None
    start = i_col - 1 if i_col > 0 else 0
    end = i_col + 2 if i_col < num_cols else num_cols - 1
    if i_row > 0:        
        top_region = matrix[i_row - 1, start : end]
        # top
        items += get_gear_region_value(matrix[i_row - 1], top_region, start, end, num_cols) if contains_digits(top_region) else [None]        
    if i_row < num_rows - 1:
        bottom_region = matrix[i_row + 1, start : end]
        # bottom
        test = False
        if i_row ==132:
            test = True
        items += get_gear_region_value(matrix[i_row + 1], bottom_region, start, end, num_cols) if contains_digits(bottom_region) else [None]
    print(matrix[i_row, i_col],i_row, i_col)
    print(items)
    items = [item for item in items if item]
    print(items)
    if len(items) != 2:
        print("-> invalid, is not gear")
        print("--------------------------------------")
        return 0
    print(items)
    print("Valid, result of multiplication: ",np.prod(items))
    print("--------------------------------------")
    return np.prod(items)

    
def get_solution_2(data):
    gear_numbers = 0
    matrix = np.array([list(line) for line in data])
    num_rows, num_cols = matrix.shape
    for idx_row, row in enumerate(matrix):
        for idx_col, cell_item in enumerate(row):
            if cell_item == '*':
                adj_number = get_adjacent_numbers(matrix, idx_row, idx_col, num_rows, num_cols)
                gear_numbers += adj_number
    return gear_numbers



file = "data/day_3.txt"

data = read_file(file)
solution_1 = get_solution_1(data)
solution_2 = get_solution_2(data)

print("Day 3 - Solution 1:", solution_1)
print("Day 3 - Solution 2:", solution_2)