from util import read_file_by_line as read_file
from present import Present

total = 0
for line in read_file('data/day02/input.txt'):
    present = Present(line.split("x"))
    total += present.surface_area

print(f"Result is <{total}>")