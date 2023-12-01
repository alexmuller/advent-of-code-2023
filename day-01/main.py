import os

def part_1(input):
    numbers = []
    for line in input:
        filtered_line = [int(char) for char in line if char.isdigit()]
        if len(filtered_line) == 0:
            continue
        elif len(filtered_line) == 1:
            numbers.append(int(f'{filtered_line[0]}{filtered_line[0]}'))
        elif len(filtered_line) == 2:
            numbers.append(int(f'{filtered_line[0]}{filtered_line[1]}'))
        else:
            numbers.append(int(f'{filtered_line[0]}{filtered_line[-1]}'))

    return sum(numbers)

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file_contents:
    input = [line for line in file_contents.read().split('\n') if line]

print(part_1(input))
