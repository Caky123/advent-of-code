from util import read_file_in_chunks

result = 0

for chunk in read_file_in_chunks('data/test.txt'):
    result += chunk.count("(") - chunk.count(")")

print(f"Result is <{result}>")
