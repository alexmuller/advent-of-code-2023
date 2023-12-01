import os

def process_line(line):
    filtered_line = [int(char) for char in line if char.isdigit()]
    if len(filtered_line) == 0:
        return None
    elif len(filtered_line) == 1:
        return int(f'{filtered_line[0]}{filtered_line[0]}')
    elif len(filtered_line) == 2:
        return int(f'{filtered_line[0]}{filtered_line[1]}')
    else:
        return int(f'{filtered_line[0]}{filtered_line[-1]}')

def part_1(input):
    numbers = []
    for line in input:
        addition = process_line(line)
        if addition:
            numbers.append(addition)

    return sum(numbers)

def part_2(input):
    new_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    numbers = []
    for line in input:
        processed_line = []
        for start_char in range(len(line)):
            remaining_line = line[start_char:]
            if remaining_line[0].isdigit():
                processed_line.append(remaining_line[0])
                continue
            else:
                for string_number in new_numbers.keys():
                    if remaining_line.startswith(string_number):
                        processed_line.append(new_numbers[string_number])
                        continue
        addition = process_line(processed_line)
        if addition:
            numbers.append(addition)

    return sum(numbers)

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file_contents:
    input = [line for line in file_contents.read().split('\n') if line]

print(part_1(input))
print(part_2(input))
