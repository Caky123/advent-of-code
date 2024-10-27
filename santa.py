from typing import Callable, Dict, Tuple, Optional
import logging

class Santa:
    visited_position: Dict[Tuple[int, int], int] = {(0, 0): 0} # Shared between instances
    def __init__(self)->None:
        self.direction: Dict[str, Callable[[], None]] = {
            "^": self.go_north,
            ">": self.go_east,
            "v": self.go_south,
            "<": self.go_west
        }
        self.position: list[int] = [0, 0] # x, y
        Santa.visited_position[(0, 0)] += 1


    def set_visited_position(self)->None:
        data: Tuple[int, int] = (self.position[0], self.position[1])
        visited_position: Optional[int] = self.visited_position.get(data)

        if visited_position:
            Santa.visited_position[data] += 1
        else:
            Santa.visited_position[data] = 1

    def go_north(self) -> None:
        self.position[1] += 1
        self.set_visited_position()

    def go_east(self) -> None:
       self.position[0] += 1
       self.set_visited_position()

    def go_south(self) -> None:
        self.position[1] -= 1
        self.set_visited_position()

    def go_west(self) -> None:
        self.position[0] -= 1
        self.set_visited_position()

    def move(self, direction_symbol: str) -> None:
        move_action = self.direction.get(direction_symbol)
        if move_action:
            move_action()
        else:
            logging.warning("Invalid direction")
    
    def visited_at_least(self, visited: int = 1 ):
        return sum(1 for val in Santa.visited_position.values() if val >= visited)
