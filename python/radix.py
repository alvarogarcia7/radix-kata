from __future__ import annotations
from dataclasses import dataclass, field
        
@dataclass
class Node:
    word: str
    is_final: bool
    children: [Node] = field(default_factory=list)


class Radix:
    _root: Node

    def __init__(self):
        self._root = Node("", False)

    def insert(self, new: str):
        self._root = Node(new, True)
