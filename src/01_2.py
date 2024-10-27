from util import read_file_in_chunks as read_file
from typing import Optional


def find_floor(floor_number: int = -1) -> Optional[int]:
    result: int = 0
    for count, chunk in enumerate(read_file('data/day01/input.txt', 1), start = 1):
        result += 1 if chunk == "(" else -1

        if result == floor_number:
            return count
    return None


def main()->None:
    floor = find_floor()
    if floor:
        print(f"Result is <{find_floor()}>")
    else:
        print(f"Floor not found")


if __name__ == "__main__":
    main()    
