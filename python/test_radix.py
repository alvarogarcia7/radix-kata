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
        radix = Radix()
        radix.insert("a")
        radix.insert("abc")

        assert FinalNode("a", True, 1) == radix._root
        assert FinalNode('bc', True, 0) == radix._root.children[0]
    
    def test_insert_sibling_nodes(self):
        radix = Radix()
        radix.insert("a")
        radix.insert("b")

        import pprint
        pprint.pprint(radix)

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

        # assert len(radix._root.children) == 2
    
    def test_insert_grandchildren_nodes(self):
        radix = Radix()
        radix.insert("a")
        radix.insert("ab")
        radix.insert("abc")
        radix.insert("abcd")

        assert FinalNode("a", True, 1) == radix._root
        assert FinalNode('b', True, 1) == radix._root.children[0]
        assert FinalNode('c', True, 1) == radix._root.children[0].children[0]
        assert FinalNode('d', True, 0) == radix._root.children[0].children[0].children[0]

    def test_insert_a_parent_node_that_matches_completely(self):
        radix = Radix()
        radix.insert("ab")
        radix.insert("a")

        assert FinalNode("a", True, 1) == radix._root
        assert FinalNode('b', True, 0) == radix._root.children[0]

