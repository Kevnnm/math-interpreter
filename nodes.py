from dataclasses import dataclass
from typing import Union

NodeType = Union


@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: NodeType
    node_b: NodeType

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubtractNode:
    node_a: NodeType
    node_b: NodeType

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: NodeType
    node_b: NodeType

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: NodeType
    node_b: NodeType

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class PlusNode:
    node: NodeType

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: NodeType

    def __repr__(self):
        return f"(-{self.node})"


NodeType = Union[MinusNode, PlusNode, MultiplyNode, DivideNode, SubtractNode, AddNode, NumberNode]
