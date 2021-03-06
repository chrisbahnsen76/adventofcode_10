# part 1 solution:
# read in the lines, determine which are corrupted, discard the corrupted lines

import sys

from line_checker import line_checker

file_path = sys.argv[1] if len(sys.argv) == 2 else ".\\input1.txt"
lines = open(file_path).read().splitlines()

for line in lines:
    status, illegal_char = line_checker.check_line(with_errors=False, line=line)
    if (status) == line_checker.LINE_IS_VALID:
        print(line)
    elif (status) == line_checker.LINE_IS_CORRUPTED:
        pass
