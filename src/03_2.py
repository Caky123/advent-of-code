
import logging
import sys

from util import read_file_in_chunks as read_file
from santa import Santa

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s', stream=sys.stdout)


def main()->None:
    santa: Santa = Santa()
    robo_santa: Santa = Santa()

    for i, direction in enumerate(read_file('data/day03/input.txt', 1), start=1):
        if i % 2 == 0:
            robo_santa.move(direction)
        else:
            santa.move(direction)

    logging.info(f"Result is <{santa.visited_at_least()}>")

if __name__ == "__main__":
    main()