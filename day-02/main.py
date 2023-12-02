import os

def parse_round(round):
    rgb = [count.strip() for count in round.strip().split(',')]
    round = {}
    for result in rgb:
        count, colour = result.split(' ')
        round[colour] = int(count)

    return round

def parse_game(line):
    game, result = line.split(':')
    rounds = [parse_round(round) for round in result.split(';')]
    return {
        'id': int(game.split(' ')[1]),
        'rounds': rounds
    }

def round_is_possible(round):
    maximums = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    return all(maximums[colour] >= round[colour] for colour in round.keys())

def game_is_possible(game):
    return all(round_is_possible(round) for round in game['rounds'])

def part_1(input):
    games = [parse_game(line) for line in input]
    return sum([game['id'] for game in games if game_is_possible(game)])

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file_contents:
    input = [line for line in file_contents.read().split('\n') if line]

print(part_1(input))
