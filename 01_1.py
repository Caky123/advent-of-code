from util import read_file_in_chunks as read_file

result = 0

for chunk in read_file('data/day01/input.txt'):
    result += chunk.count("(") - chunk.count(")")

print(f"Result is <{result}>")
