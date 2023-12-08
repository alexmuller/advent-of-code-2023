import os

def process_card(input):
    card_id = int(input.split(':')[0].split(' ')[-1])
    winners = [int(value) for value in input.split('|')[0].split(':')[1].strip().split(' ') if value]
    numbers = [int(value) for value in input.split('|')[1].strip().split(' ') if value]
    winner_count = len([value for value in numbers if value in winners])
    if winner_count:
        points = 1
        points = points * 2 ** (winner_count - 1)
    else:
        points = 0
    return {
        'card_id': card_id,
        'winners': winners,
        'numbers': numbers,
        'winner_count': winner_count,
        'points': points,
        'count': 1
    }

def part_1(input):
    processed_cards = [process_card(day) for day in input]
    cards = dict(zip([card['card_id'] for card in processed_cards], processed_cards))
    total_points = sum([card['points'] for card in cards.values()])
    return total_points

def part_2(input):
    processed_cards = [process_card(day) for day in input]
    cards = dict(zip([card['card_id'] for card in processed_cards], processed_cards))
    for card in cards.values():
        cards_to_add = [i+card['card_id']+1 for i in range(card['winner_count'])] * card['count']
        for adding_card in cards_to_add:
            cards[adding_card]['count'] += 1
    total_cards = sum([card['count'] for card in cards.values()])
    return total_cards

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file_contents:
    input = [line for line in file_contents.read().split('\n') if line]

print(part_1(input))
print(part_2(input))
