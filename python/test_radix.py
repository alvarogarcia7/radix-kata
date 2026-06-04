from radix import Node, Radix, FinalNode

class TestRadix:
    def test_empty_node(self):
        node = Node("a", True)
        assert node.word == "a"
        assert node.children == []
        assert node.is_final

    def test_node_with_all_arguments(self):
        node = Node("a", True, ['a'])
        assert node.word == "a"
        assert node.children == ['a']
        assert node.is_final
    
    def test_insert_only_word(self):
        radix = Radix()
        radix.insert("a")

        assert radix._root == Node("a", True)
    
    def test_insert_children_nodes(self):
        radix = Radix()
        radix.insert("a")
        radix.insert("abc")

        assert FinalNode("a") == radix._root
        assert FinalNode('bc') == radix._root.children[0]
    
    def test_insert_sibling_nodes(self):
        radix = Radix()
        radix.insert("a")
        radix.insert("b")

        assert FinalNode("a") == radix._root.children[0]
        assert FinalNode('b') == radix._root.children[1]
