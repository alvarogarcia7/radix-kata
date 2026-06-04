import itertools
import pprint
from typing import Iterator

from radix import Node, Radix, FinalNode


class TestRadix:
    def test_empty_node(self):
        node = Node("a", True)
        assert node.word == "a"
        assert node.children == []
        assert node.is_final

    def test_node_with_all_arguments(self):
        node = Node("a", True, [Node("a", True)])
        assert node.word == "a"
        assert node.children == [Node("a", True)]
        assert node.is_final
    
    def test_insert_only_word(self):
        radix = Radix()
        radix.insert("a")

        assert FinalNode("a", True, 0) == radix._root
    
    def test_insert_children_nodes(self):
        for radix in self.permute_insert(["a", "abc"]):
            assert FinalNode("a", True, 1) == radix._root
            assert FinalNode('bc', True, 0) == radix._root.children[0]

    # def test_insert_sibling_nodes(self):
    #     for radix in self.permute_insert(["a", "b"]):
    #         pprint.pprint(radix)
    #         assert FinalNode("", False, 2) == radix._root
    #         assert FinalNode("a", True, 0) == radix._root.children[0]
    #         assert FinalNode('b', True, 0) == radix._root.children[1]

    def test_insert_sibling_nodes(self):
        radix = Radix()
        radix.insert("a")
        radix.insert("b")

        assert FinalNode("", False, 2) == radix._root
        assert FinalNode("a", True, 0) == radix._root.children[0]
        assert FinalNode('b', True, 0) == radix._root.children[1]

    def test_insert_niece_nodes(self):
        radix = Radix()
        radix.insert("a")
        radix.insert("abc")
        radix.insert("ad")

        assert FinalNode("a", True, 2) == radix._root
        assert FinalNode('bc', True, 0) == radix._root.children[0]
        assert FinalNode('d', True, 0) == radix._root.children[1]

    def test_insert_grandchildren_nodes(self):
        radix = Radix()
        radix.insert("a")
        radix.insert("ab")
        radix.insert("abc")
        radix.insert("abcd")

        pprint.pprint(radix)

        assert FinalNode("a", True, 1) == radix._root
        assert FinalNode('b', True, 1) == radix._root.children[0]
        assert FinalNode('c', True, 1) == radix._root.children[0].children[0]
        assert FinalNode('d', True, 0) == radix._root.children[0].children[0].children[0]

    # def test_insert_niece_nodes(self):
    #     for radix in self.permute_insert(["a", "ad", "abc"]):
    #         pprint.pprint(radix)
    #         assert FinalNode("a", True, 2) == radix._root
    #         assert FinalNode('bc', True, 0) == radix._root.children[0]
    #         assert FinalNode('d', True, 0) == radix._root.children[1]
    #
    # def test_insert_grandchildren_nodes(self):
    #     for radix in self.permute_insert(["a", "ab", "abc", "abcd"]):
    #         assert FinalNode("a", True, 1) == radix._root
    #         assert FinalNode('b', True, 1) == radix._root.children[0]
    #         assert FinalNode('c', True, 1) == radix._root.children[0].children[0]
    #         assert FinalNode('d', True, 0) == radix._root.children[0].children[0].children[0]

    def test_insert_a_parent_node_that_matches_completely(self):
        for radix in self.permute_insert(["abc", "a"]):
            assert FinalNode("a", True, 1) == radix._root
            assert FinalNode('bc', True, 0) == radix._root.children[0]


    def test_insert_a_parent_node_that_matches_completely_with_multiple_letters(self):
        for radix in self.permute_insert(["abcd", "ab"]):
            assert FinalNode("ab", True, 1) == radix._root
            assert FinalNode('cd', True, 0) == radix._root.children[0]


    def test_insert_a_child_node_that_matches_partially(self):
        for radix in self.permute_insert(["abcd", "a", "ab"]):
            assert FinalNode("a", True, 1) == radix._root
            assert FinalNode("b", True, 1) == radix._root.children[0]
            assert FinalNode('cd', True, 0) == radix._root.children[0].children[0]

    def test_insert_two_nodes_sharing_a_non_final_word(self):
        for radix in self.permute_insert(["ac", "ab"]):
            assert FinalNode("a", False, 2) == radix._root
            assert FinalNode("b", True, 0) == radix._root.children[0]
            assert FinalNode("c", True, 0) == radix._root.children[1]

    @staticmethod
    def permute_insert(news: list[str]) -> Iterator[Radix]:
        permutation: tuple[str]
        for permutation in itertools.permutations(news):
            radix = Radix()
            for element in permutation:
                radix.insert(element)
            yield radix
