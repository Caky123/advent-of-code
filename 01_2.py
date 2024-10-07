from util import read_file_in_chunks as read_file

result = 0
index = 0

for count, chunk in enumerate(read_file('data/day01/input.txt', 1), start = 1):
    result += chunk.count("(") - chunk.count(")")

    if result == -1:
        index = count
        break

print(f"Result is <{index}>")
