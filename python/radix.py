from __future__ import annotations
from dataclasses import dataclass, field
        
@dataclass
class Node:
    word: str
    is_final: bool
    children: [Node] = field(default_factory=list)

    def __eq__(self, o: Any):
        return self.word == o.word and self.is_final == o.is_final

    def __deep_eq__(self, o: Any):
        return self == o and self.children == o.children

@dataclass
class FinalNode:
    word: str
    is_final: bool = field(default_factory=lambda: True)

    def __eq__(self, o: Any):
        return self.word == o.word and self.is_final == o.is_final

class Radix:
    _root: Node | None

    def __init__(self):
        self._root = None

    def insert(self, new: str):
        if self._root is None:
            self._root = Node(new, True)
        else:
            if new.startswith(self._root.word):
                rest_of_word = new.split(self._root.word, 1)[1]
                self._root.children.append(Node(rest_of_word, True))
