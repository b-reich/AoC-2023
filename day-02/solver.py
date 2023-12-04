#!/usr/bin/python3

from collections import defaultdict
from typing import Dict, List
from functools import reduce

desired_counts = defaultdict(int, {"red": 12, "blue": 14, "green": 13})


def main():
    games: Dict[str, List[Dict[str, int]]] = {}
    with open('day-02/input.txt', 'r') as file:
        for line in file:
            game_str, pull_str = line.split(": ")
            pulls = pull_str.split("; ")
            game_id = int(game_str.strip().split(" ")[-1])

            games[game_id] = []

            for pull in pulls:
                colors = pull.split(", ")
                round_dict = {}

                for color in colors:
                    count, color_name = color.split(" ")
                    round_dict[color_name.strip()] = int(count)

                games[game_id].append(round_dict)

    # 1st part
    # possible_games = [game_id for game_id, pulls in games.items() if all(
    #     all(round_dict[color] <= desired_counts[color] for color in round_dict) for round_dict in pulls)]

    # 2nd part
    total_power = 0
    for game_id, pulls in games.items():
        max_counts = {
            color: max(round_dict.get(color, 0) for round_dict in pulls) for color in desired_counts
        }
        power = reduce(lambda x, y: x * y, max_counts.values())
        total_power += power
    return total_power


if __name__ == "__main__":
    print(main())
