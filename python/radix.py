from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Node:
    word: str
    is_final: bool
    children: [Node] = field(default_factory=list)

    def __eq__(self, o: Any):
        return self.word == o.word and self.is_final == o.is_final

    def __deep_eq__(self, o: Any):
        return self == o and self.children == o.children

    def __repr__(self):
        is_f = "F" if self.is_final else " "
        return f"[{is_f}] {self.word} {len(self.children)}\n" + "\n".join([c.__repr__() for c in self.children])

    def insert(self, new: str):
        if new.startswith(self.word):
            rest_of_word = new.split(self.word, 1)[1]
            import os

            for child in self.children:
                children_words = []
                children_words.append(rest_of_word)
                children_words.append(child.word)
                result = os.path.commonprefix(children_words)
                if result != '':
                    print(f"case insert {new} - result != []")
                    # has a common prefix with one of the children
                    child.insert(rest_of_word)
                    return
            print(f"case insert {new} - last append")
            self.children.append(Node(rest_of_word, True))
        else:
            self.children.append(Node(new, True))


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

    def __repr__(self):
        return "\n".join([c.__repr__() for c in [[self._root] + self._root.children]])

    def insert(self, new: str):
        if self._root is None:
            self._root = Node(new, True)
            return

        if new.startswith(self._root.word):
            rest_of_word = new.split(self._root.word, 1)[1]
            print(rest_of_word)
            import os

            for child in self._root.children:
                children_words = []
                children_words.append(rest_of_word)
                children_words.append(child.word)
                result = os.path.commonprefix(children_words)
                print(result)
                if result != '':
                    # has a common prefix with one of the children
                    child.insert(rest_of_word)
                    return

            print(f"Case {rest_of_word} PASSING AFTER FOR")
            self._root.children.append(Node(rest_of_word, True))
        else:
            new_root = Node("", False)
            new_root.children.append(self._root)
            self._root = new_root

            self._root.children.append(Node(new, True))
