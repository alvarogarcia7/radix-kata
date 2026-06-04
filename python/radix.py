from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import os


@dataclass
class Node:
    word: str
    is_final: bool
    children: list[Node] = field(default_factory=list)

    def __eq__(self, o: Any):
        return self.word == o.word and self.is_final == o.is_final

    def __deep_eq__(self, o: Any):
        return self == o and self.children == o.children

    def __repr__(self, depth=0):
        is_f = "F" if self.is_final else " "
        repr_for_parent = f"{'\t' * depth}[{is_f}] {self.word}"
        if len(self.children) == 0:
            return repr_for_parent
        else:
            repr_for_parent += "\n"
        else_ = (f"{len(self.children)} children:\n" + "".join(
            [c.__repr__(depth + 1) for c in self.children]) if self.children else "")
        return repr_for_parent + else_

    def insert(self, new: str):
        self.insert_child_or_sibling(new)

    def insert_child_or_sibling(self, new: str):
        if new.startswith(self.word):
            rest_of_word = new.split(self.word, 1)[1]
            inserted = False
            for child in self.children:
                shared_prefix_for_child = os.path.commonprefix([rest_of_word, child.word])
                if shared_prefix_for_child != '':
                    child.insert(rest_of_word)
                    inserted = True
            if not inserted:
                self.children.append(Node(rest_of_word, True))
        else:
            self.children.append(Node(new, True))


@dataclass
class FinalNode:
    word: str
    is_final: bool = field(default_factory=lambda: True)
    children_size: int = field(default_factory=lambda: 0)

    def __eq__(self, o: Any):
        return self.word == o.word and self.is_final == o.is_final and self.children_size == len(o.children)

class Radix:
    _root: Node | None

    def __init__(self):
        self._root = None

    def __repr__(self):
        return self._root.__repr__()

    def insert(self, new: str):
        if self._root is None:
            self._root = Node(new, True)
            return

        if self._root.word.startswith(new):
            new_root = Node(new, True)
            previous_root = self._root
            previous_root.word = previous_root.word[len(new):]
            new_root.children.append(previous_root)
            self._root = new_root
        elif new.startswith(self._root.word) :
            self._root.insert_child_or_sibling(new)
        else:
            new_root = Node("", False)
            new_root.children.append(self._root)
            self._root = new_root

            self._root.children.append(Node(new, True))
