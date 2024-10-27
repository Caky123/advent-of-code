from util import read_file_in_chunks as read_file


def find_final_floor():
    result = 0
    for chunk in read_file('data/day01/input.txt'):
        result += chunk.count("(") - chunk.count(")")
    return result


def main():
    print(f"Result is <{find_final_floor()}>")


if __name__ == "__main__":
    main()