import sys
from line_checker import line_checker

file_path = sys.argv[1] if len(sys.argv) == 2 else ".\\input1.txt"
lines = open(file_path).read().splitlines()

scoring_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}

line_checker = line_checker()


def get_points(c):
    return (scoring_dict.get(c) if scoring_dict.get(c) else 0)


def calculate_points(lines):
    score = 0
    for line in lines:
        status, illegal_char = line_checker.check_line(line)
        if status == line_checker.LINE_IS_CORRUPTED:
            score += get_points(illegal_char)

    return score


print(calculate_points(lines))
