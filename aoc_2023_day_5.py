### https://adventofcode.com/2023/day/5


def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return list(filter(None, [line.strip() for line in f_in.readlines()]))
    

def get_almanac_dict(data):
    almanac = dict()
    dict_key = ""
    for line in data:
        seed_str = "seeds: "
        if line.startswith(seed_str):
            seeds_sol_1 = list(map(int, line.replace(seed_str, '').strip().split(' ')))
            seeds_sol_2 = list(zip(seeds_sol_1[::2], seeds_sol_1[1::2]))
            continue
        if "map:" in line:
            dict_key = line.replace(" map:", "").replace("-to-", "_2_")
            almanac[dict_key] = []
            continue
        dest_start, source_start, length = line.strip().split(' ')
        almanac[dict_key] += [{
                "dest_start": int(dest_start), 
                "source_start": int(source_start), 
                "length": int(length)
            }]
    return almanac, seeds_sol_1, seeds_sol_2
    
    
def get_solution_1(almanac, seeds):
    almanac_chain = list(almanac)
#     print(seeds, "seeds")
    for mapping in almanac_chain:
        for seed_idx, seed in enumerate(seeds):
            for item in almanac[mapping]:
                start = item["source_start"]
                end = item["source_start"] + item["length"]
                if seed in range(start, end):
                    seeds[seed_idx] = item["dest_start"] + seed - start
                    continue
#         print(seeds, mapping)
    return min(seeds)

def get_solution_2(almanac, seeds):
    min_loc = None
    almanac_chain = list(almanac)
#     print(seeds, "seeds")        

    for seed_start, _len in seeds:   
        pair_idx = seeds.index((seed_start, _len))
        print(f"Run {pair_idx + 1}. pair...")
        seed_range = list(range(seed_start, seed_start + _len))
        for seed_idx, seed in enumerate(seed_range):
            for mapping in almanac_chain:
                for item in almanac[mapping]:
                    start = item["source_start"]
                    end = item["source_start"] + item["length"]
                    if seed in range(start, end):
#                         print(seed, mapping, item)
                        seed_range[seed_idx] = item["dest_start"] + seed - start -1
                        continue
                curr_min = min(seed_range)
                min_loc = curr_min if not min_loc or curr_min < min_loc else min_loc
#                 print(seed_range, mapping)
    return min_loc


file = "data/day_5.txt"
# file = "data/day_5_test.txt"

almanac_data, seeds_solution_1, seeds_solution_2 = get_almanac_dict(read_file(file))
solution_1 = get_solution_1(almanac_data, seeds_solution_1)

# TODO
# solution_2 = get_solution_2(almanac_data, seeds_solution_2)

print("Day 5 - Solution 1:", solution_1) 

# TODO
# print("Day 5 - Solution 2:", solution_2) # low: 31.918.867, high: 3.398.490.369