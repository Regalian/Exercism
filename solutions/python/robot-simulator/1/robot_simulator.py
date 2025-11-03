from enum import Enum


class Errormessages(Enum):
    INVALID_INSTRUCTION = "Invalid instruction"


# Globals for the directions
# Change the values as you see fit
EAST = 1, 0
NORTH = 0, 1
WEST = -1, 0
SOUTH = 0, -1


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
        self._directions = [NORTH, EAST, SOUTH, WEST]
        while self._directions[0] != self.direction:
            self._directions = self._directions[1:] + self._directions[:1]

    def move(self, instruction: str) -> None:
        """ Process a series of moves by the robot.

        An instrcution is a string, e.g. 'RAALAL' where 
        'R' -> rotate right
        'L' -> rotate left
        'A' -> move forward one step

        Args:
            instruction: str: A sequence of moves
        
        raises:
            ValueError: unrecognised instruction
        """

        for action in instruction.upper():
            match action:
                case "A":
                    self.coordinates = (
                        self.coordinates[0] + self.direction[0],
                        self.coordinates[1] + self.direction[1],
                    )
                case "R":
                    self._directions = self._directions[1:] + self._directions[:1]
                    self.direction = self._directions[0]
                case "L":
                    self._directions = self._directions[-1:] + self._directions[:-1]
                    self.direction = self._directions[0]
                case _:
                    raise ValueError(Errormessages.INVALID_INSTRUCTION.value)
