import os

def process_day(input):
    winners = [int(value) for value in input.split('|')[0].split(':')[1].strip().split(' ') if value]
    numbers = [int(value) for value in input.split('|')[1].strip().split(' ') if value]
    winner_count = len([value for value in numbers if value in winners])
    if winner_count:
        points = 1
        points = points * 2 ** (winner_count - 1)
    else:
        points = 0
    return {
        'winners': winners,
        'numbers': numbers,
        'winner_count': winner_count,
        'points': points
    }

def part_1(input):
    days = [process_day(day) for day in input]
    total_points = sum([day['points'] for day in days])
    return total_points

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file_contents:
    input = [line for line in file_contents.read().split('\n') if line]

print(part_1(input))
