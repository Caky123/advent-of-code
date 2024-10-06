from util import read_file_in_chunks as read_file

result = 0
index = 0

for chunk in read_file('data/day01/input.txt', 1):
    result += chunk.count("(") - chunk.count(")")
    index += 1

    if result == -1:
        break

print(f"Result is <{index}>")
