from dataclasses import dataclass
from util import read_file_by_line as read_file
from present import Present

@dataclass
class Result:
    surface_area: int
    feet_of_ribbon: int

def calc_total_presents_param():
    total_surface_area = 0
    total_feet_ribbon = 0
    for line in read_file('data/day02/input.txt'):
        try:
            present = Present([int(x) for x in line.split("x")])
            total_surface_area += present.calc_surface_area()
            total_feet_ribbon += present.feet_of_ribbon()
        except Exception as e:
            print(e)
    return Result(surface_area = total_surface_area, feet_of_ribbon = total_feet_ribbon)

def main():
    result: Result = calc_total_presents_param()
    print(f"Result (square feet of wrapping paper) is <{result.surface_area}>")
    print(f"Result (feet of ribbon) is <{result.feet_of_ribbon}>")

if __name__ == "__main__":
    main()