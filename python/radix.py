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
            repr_for_parent += " - "
        else_ = (f"{len(self.children)} children:\n" + "\n".join(
            [c.__repr__(depth + 1) for c in self.children]) if self.children else "")
        return repr_for_parent + else_

    def insert(self, new: str):
        self.insert_child_or_sibling(new)

    def insert_child_or_sibling(self, new: str) -> Node:
        if self.word.startswith(new):
            new_root = Node(new, True)
            previous_root = self
            previous_root.word = previous_root.word[len(new):]
            new_root.children.append(previous_root)
            return new_root
        elif new.startswith(self.word):
            rest_of_word = new.split(self.word, 1)[1]
            inserted = False
            for child in self.children:
                shared_prefix_for_child = os.path.commonprefix([rest_of_word, child.word])
                if shared_prefix_for_child != '':
                    child_contains_more_than_shared_prefix = len(child.word) > len(shared_prefix_for_child)
                    if child_contains_more_than_shared_prefix:
                        intermediate_node = Node(shared_prefix_for_child, child.is_final, [child])
                        child.word = child.word[len(shared_prefix_for_child):]
                        self.children.append(intermediate_node)
                        self.children.remove(child)
                        inserted = True
                    else:
                        child.insert(rest_of_word)
                        inserted = True
            if not inserted:
                self.children.append(Node(rest_of_word, True))
            return self
        else:
            self.children.append(Node(new, True))
            return self


@dataclass
class FinalNode:
    word: str
    is_final: bool = field(default_factory=lambda: True)
    children_size: int = field(default_factory=lambda: 0)

    def __eq__(self, o: Any):
        return self.word == o.word and self.is_final == o.is_final and self.children_size == len(o.children)

    def __repr__(self, depth=0):
        is_f = "F" if self.is_final else " "
        return f"{'\t' * depth}[{is_f}] {self.word} {self.children_size} children"

class Radix:
    _root: Node | None

    def __init__(self):
        self._root = None

    def __repr__(self):
        return "\n" + self._root.__repr__()

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
            self._root = self._root.insert_child_or_sibling(new)
        elif self._root_or_children_have_a_common_subprefix(self._root, new):
            inserted = False
            root_word = self._root.word
            shared_prefix_for_root = os.path.commonprefix([new, root_word])
            if shared_prefix_for_root != '' and shared_prefix_for_root != root_word:
                root_contains_more_than_shared_prefix = len(root_word) > len(shared_prefix_for_root)
                if root_contains_more_than_shared_prefix:
                    new_without_prefix = new[len(shared_prefix_for_root):]
                    intermediate_node = Node(shared_prefix_for_root, False)
                    rest_of_root_word = root_word[len(shared_prefix_for_root):]
                    node_rest_of_root_word = Node(rest_of_root_word, True, self._root.children)

                    node_new = Node(new_without_prefix, True)
                    if new_without_prefix < rest_of_root_word:
                        intermediate_node.children.append(node_new)
                        intermediate_node.children.append(node_rest_of_root_word)
                    else:
                        intermediate_node.children.append(node_rest_of_root_word)
                        intermediate_node.children.append(node_new)
                    inserted = True
                    self._root = intermediate_node
            if inserted:
                return
        else:
            new_root = Node("", False)
            new_root.children.append(self._root)
            self._root = new_root

            self._root.children.append(Node(new, True))

    @staticmethod
    def _root_or_children_have_a_common_subprefix(_root, new) -> bool:
        shared_prefix_for_root = os.path.commonprefix([new, _root.word])
        if shared_prefix_for_root != '':
            return True
        for child in _root.children:
            shared_prefix_for_child = os.path.commonprefix([new, child.word])
            if shared_prefix_for_child != '':
                return True
        return False
