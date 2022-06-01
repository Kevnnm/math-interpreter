from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    L_PAREN = 5
    R_PAREN = 6


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")

