#You’ll use this file throughout the rest of this step to define tic-tac-toe domain model objects.
import enum
from dataclasses import dataclass

class Mark(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> "Mark":
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT