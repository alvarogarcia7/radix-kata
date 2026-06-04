from radix import Node

class TestRadix:
    def test_true(self):
        assert True == True

    def test_empty_node(self):
        node = Node("a", True)
        assert node.word == "a"
        assert node.children == []
        assert node.is_final

