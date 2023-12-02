### https://adventofcode.com/2023/day/1


import re



TXT_2_DIGIT = {
    "one": "1", 
    "two": "2", 
    "three": "3", 
    "four": "4", 
    "five": "5", 
    "six": "6", 
    "seven": "7", 
    "eight": "8", 
    "nine": "9"
}


def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return [line.strip() for line in f_in.readlines()]
    

def get_solution_1(data):
    digits = list(filter(None, [''.join(re.findall(r'\d+', item)) for item in data]))
    return sum([int(item[:1] + item[-1]) for item in digits])
        
    
def get_solution_2(data):
    data_preprocessed = []    
    for item in data:
        for key, digit in TXT_2_DIGIT.items():
            item = item.replace(key, key[:-1] + str(digit) + key[1:])
        data_preprocessed.append(item)
    return get_solution_1(data_preprocessed)




file_1 = "data/day_1_1.txt"
file_2 = "data/day_1_2.txt"

data_1 = read_file(file_1)
solution_1 = get_solution_1(data_1)

data_2 = read_file(file_2)
solution_2 = get_solution_2(data_2)

print("Solution 1-1:", solution_1)
print("Solution 1-2:", solution_2)
