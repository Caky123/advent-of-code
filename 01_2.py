from util import read_file_in_chunks as read_file


def find_floor(floor_number: int = -1) -> int:
    result: int = 0
    for count, chunk in enumerate(read_file('data/day01/input.txt', 1), start = 1):
        result += 1 if chunk == "(" else -1

        if result == floor_number:
            return count


def main():
    print(f"Result is <{find_floor()}>")


if __name__ == "__main__":
    main()    
