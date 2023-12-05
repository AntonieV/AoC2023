### https://adventofcode.com/2023/day/4

import re



def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return list(filter(None, [line.strip() for line in f_in.readlines()]))
    

def get_cards(data):
    cards = dict()
    for item in data:
        card_id, values = item.strip().split(':')
        card_id = card_id.replace('Card', '').strip()
        win_numbers, card_numbers = values.strip().split('|')         
        win_numbers = list(filter(None, re.split(r'\s+', win_numbers)))
        card_numbers = list(filter(None, re.split(r'\s+', card_numbers)))
        cards[card_id] = {"win_numbers": win_numbers, "card_numbers": card_numbers, "count": 1}
    return cards
    
    
def get_solution_1(cards):
    points = 0
    for card_id, card_vals in cards.items():
        n_win = len(list(set(card_vals["win_numbers"]) & set(card_vals["card_numbers"])))
        points += 2**(n_win - 1) if n_win > 0 else 0
    return points
        
    
def get_solution_2(cards):
    for card_id, card_vals in cards.items():
        n_win = len(list(set(card_vals["win_numbers"]) & set(card_vals["card_numbers"])))
        for i in range(1, n_win + 1):
            cards[str(int(card_id)+i)]["count"] += 1 * card_vals["count"]
    return sum([card_vals["count"] for card_id, card_vals in cards.items()])



file = "data/day_4.txt"

data = get_cards(read_file(file))
                    
solution_1 = get_solution_1(data)
solution_2 = get_solution_2(data)

print("Day 4 - Solution 1:", solution_1)
print("Day 4 - Solution 2:", solution_2)