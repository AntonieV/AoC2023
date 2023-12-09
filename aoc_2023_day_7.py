### https://adventofcode.com/2023/day/7

import pandas as pd


CARD_SET_TYPES = {
    "Five of a kind": 6,
    "Four of a kind": 5,
    "Full house": 4,
    "Three of a kind": 3,
    "Two pair": 2,
    "One pair": 1,
    "High card": 0
}

TRANSLATION = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

CARD_STRENGTH = dict(zip(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"], TRANSLATION))

CARD_STRENGTH_SOL_2 = dict(zip(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"], TRANSLATION))



def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return list(filter(None, [line.strip() for line in f_in.readlines()]))
    

def get_counts(cards):
    return dict(set([(card, cards.count(card)) for card in cards]))
    
    
def get_counts_for_solution_2(cards, counts):
    num_j = cards.count("J")
    if num_j == 5:
        return counts
    counts_sorted = sorted(counts, key=counts.get, reverse=True)
    highest, next_highest = counts_sorted[0], counts_sorted[1]
    if highest != "J":
        counts[highest] += num_j
    else:
        counts[next_highest] += num_j
    counts.pop("J")
    return counts
    
    
def get_cards_type(cards, sol_id=""):   
    counts = get_counts(cards) 
    if sol_id == "sol_2" and "J" in counts:
        counts = get_counts_for_solution_2(cards, counts)          
        
    counts = sorted(counts.values(), reverse=True)    
    print(counts)
    highest = counts[0]      
    if len(counts) > 1:
        next_highest = counts[1]
        
    card_set = "High card"
    if highest == 5:
        card_set = "Five of a kind"
    elif highest == 4:
        card_set = "Four of a kind"
    elif highest == 3 and next_highest == 2:
        card_set = "Full house"
    elif highest == 3 and next_highest == 1:
        card_set = "Three of a kind"
    elif highest == 2 and next_highest == 2:
        card_set = "Two pair"
    elif highest == 2 and next_highest == 1:
        card_set = "One pair"
    return card_set, CARD_SET_TYPES[card_set]

def translate_card_strenght(cards, sol_id=""):
    if sol_id == "sol_2":
        return ''.join([CARD_STRENGTH_SOL_2[char] for char in list(cards)])
    return ''.join([CARD_STRENGTH[char] for char in list(cards)])
    
    
def parse_input(data, sol_id=""):
    card_data = []
    cols = ["cards", "bid", "cards_type", "cards_type_score", "card_strength", "rank"]
    for line in data:
        cards, bid = line.strip().split(' ')
        cards_type, cards_type_score = get_cards_type(cards, sol_id)
        card_strength = translate_card_strenght(cards, sol_id)
        rank = None
        card_data.append(dict(zip(cols, [cards, int(bid), cards_type, cards_type_score, card_strength, rank])))        
    return pd.DataFrame(card_data, columns=cols)    
    

def get_solution(df):
    df = df.sort_values(by=["cards_type_score", "card_strength"], ascending=[False, True])
    df["rank"] = list(range(1, len(df["cards"]) + 1))[::-1]
    df["bid_rank"] = df["bid"] * df["rank"]
    display(df)
    return sum(df["bid_rank"])



file = "data/day_7.txt"
# file = "data/day_7_test.txt"

data = read_file(file)
df_data_1 = parse_input(data)
df_data_2 = parse_input(data, "sol_2")

solution_1 = get_solution(df_data_1)
solution_2 = get_solution(df_data_2)

print("Day 7 - Solution 1:", solution_1)  # 249748283
print("Day 7 - Solution 2:", solution_2)  # 248029057