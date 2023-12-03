import itertools
import os

def coordinates_of_symbols(input):
    coordinates = {}

    for y_value, line in enumerate(input):
        for x_value, character in enumerate(line):
            if character == '.' or character.isdigit():
                continue
            else:
                for x_s in (x_value-1, x_value, x_value+1):
                    for y_s in (y_value-1, y_value, y_value+1):
                        coordinates[(x_s, y_s)] = character

    return coordinates

def number_locations(input):
    numbers = []
    current_number = ''
    current_number_coordinates = set()
    for y_value, line in enumerate(input):
        for x_value, character in enumerate(line):
            if not character.isdigit():
                if current_number:
                    numbers.append({
                        'number': int(current_number),
                        'coordinates': current_number_coordinates
                    })
                current_number = ''
                current_number_coordinates = set()
                continue
            else:
                current_number_coordinates.add((x_value, y_value))
                current_number = f'{current_number}{character}'

    return numbers

def part_1(input):
    symbols = coordinates_of_symbols(input)
    numbers = number_locations(input)
    numbers_touching_symbol = []
    total = 0
    for number in numbers:
        number_is_found = False
        for coordinates in number['coordinates']:
            if coordinates in symbols and not number_is_found:
                total += number['number']
                number_is_found = True
    return total

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file_contents:
    input = [line for line in file_contents.read().split('\n') if line]

print(part_1(input))
