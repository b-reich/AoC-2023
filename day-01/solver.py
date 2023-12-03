#!/usr/bin/python3

import re

# pattern = r"(\d)"
pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"

word_to_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def convert_to_number(match: str):
    return str(word_to_number.get(match))


def main():
    sum = 0
    counter = 0
    with open('day-01/input.txt', 'r') as file:
        for line in file:
            counter += 1
            print(f"Line: {counter}: {line}")
            matches = re.findall(pattern, line)
            # matches = re.search(pattern, line)
            # print(matches.group())
            first_digit: str = matches[0]
            last_digit: str = matches[-1]

            print(f"First: {first_digit}, Last: {last_digit}")
            if not first_digit.isnumeric():
                first_digit = convert_to_number(first_digit)

            if not last_digit.isnumeric():
                last_digit = convert_to_number(last_digit)

            # Combine to form a two-digit number
            number = int(str(first_digit) + str(last_digit))
            print(f"Number is: {number}")

            # Add to the total
            sum += number

    return sum


if __name__ == "__main__":
    print(main())
