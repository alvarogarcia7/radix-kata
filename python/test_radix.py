from radix import Node, Radix

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
