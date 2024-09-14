import unittest
from bst import BinarySearchTreeNode

class TestBinarySearchTreeNode(unittest.TestCase):
    def setUp(self):
        self.root = BinarySearchTreeNode(10)
        values = [5, 15, 2, 7, 12, 20]
        for value in values:
            self.root.insert(value)


    def test_insert(self):
        self.root.insert(8)
        self.assertTrue(self.root.contains(8), "Value 8 should be present in the tree after insertion.")

        self.root.insert(1)
        self.assertTrue(self.root.contains(1), "Value 1 should be present in the tree after insertion.")


    def test_contains(self):
        self.assertTrue(self.root.contains(10), "Value 10 should be present in the tree.")
        self.assertTrue(self.root.contains(5), "Value 5 should be present in the tree.")
        self.assertTrue(self.root.contains(15), "Value 15 should be present in the tree.")

        self.assertFalse(self.root.contains(100), "Value 100 should not be present in the tree.")
        self.assertFalse(self.root.contains(-5), "Value -5 should not be present in the tree.")


    def test_delete_root(self):
        root = BinarySearchTreeNode(10)
        values = [5, 15, 2, 7, 12, 20]
        for value in values:
            root.insert(value)

        self.assertEqual(root.size(), 7, "Size of the tree is not as expected.")
        root.delete(10)
        self.assertFalse(root.contains(10), "Value 10 should not be present in the tree after deletion.")
        self.assertEqual(root.size(), 6, "Size of the tree is not as expected.")
        for value in values:
            self.assertTrue(root.contains(value), f"Value {value} should be present in the tree.")


    def test_delete_leaf(self):
        root = BinarySearchTreeNode(10)
        values = [5, 15, 2, 7, 12, 20]
        for value in values:
            root.insert(value)

        self.assertEqual(root.size(), 7, "Size of the tree is not as expected.")
        root.delete(2)
        self.assertFalse(root.contains(2), "Value 2 should not be present in the tree after deletion.")
        self.assertEqual(root.size(), 6, "Size of the tree is not as expected.")
        for value in values:
            if value == 2:
                continue

            self.assertTrue(root.contains(value), f"Value {value} should be present in the tree.")


    def test_delete_node_with_one_child(self):
        root = BinarySearchTreeNode(10)
        values = [5, 15, 2, 7, 12, 20, 1]
        for value in values:
            root.insert(value)

        self.assertEqual(root.size(), 8, "Size of the tree is not as expected.")
        root.delete(2)
        self.assertFalse(root.contains(2), "Value 2 should not be present in the tree after deletion.")
        self.assertEqual(root.size(), 7, "Size of the tree is not as expected.")
        for value in values:
            if value == 2:
                continue

            self.assertTrue(root.contains(value), f"Value {value} should be present in the tree.")


    def test_delete_node_with_two_children(self):
        root = BinarySearchTreeNode(10)
        values = [5, 15, 2, 7, 12, 20]
        for value in values:
            root.insert(value)

        self.assertEqual(root.size(), 7, "Size of the tree is not as expected.")
        root.delete(15)
        self.assertFalse(root.contains(15), "Value 15 should not be present in the tree after deletion.")
        self.assertEqual(root.size(), 6, "Size of the tree is not as expected.")
        for value in values:
            if value == 15:
                continue

            self.assertTrue(root.contains(value), f"Value {value} should be present in the tree.")


    def test_height(self):
        result = self.root.height()
        self.assertEqual(result, 3, "Height of the tree is not as expected.")


    def test_size(self):
        result = self.root.size()
        self.assertEqual(result, 7, "Size of the tree is not as expected.")


    def test_min(self):
        result = self.root.min()
        self.assertEqual(result, 2, "Minimum value in the tree is not as expected.")


    def test_max(self):
        result = self.root.max()
        self.assertEqual(result, 20, "Maximum value in the tree is not as expected.")


    def test_is_balanced(self):
        self.assertTrue(self.root.is_balanced(), "Tree should be balanced.")


    def test_inorder_traversal(self):
        result = self.root.traverse_inorder()
        expected_result = [2, 5, 7, 10, 12, 15, 20]
        self.assertEqual(result, expected_result, "Inorder traversal did not return the expected result.")


    def test_preorder_traversal(self):
        result = self.root.traverse_preorder()
        expected_result = [10, 5, 2, 7, 15, 12, 20]
        self.assertEqual(result, expected_result, "Preorder traversal did not return the expected result.")


    def test_postorder_traversal(self):
        result = self.root.traverse_postorder()
        expected_result = [2, 7, 5, 12, 20, 15, 10]
        self.assertEqual(result, expected_result, "Postorder traversal did not return the expected result.")


    def test_level_traversal(self):
        result = self.root.traverse_level()
        expected_result = [10, 5, 15, 2, 7, 12, 20]
        self.assertEqual(result, expected_result, "Level traversal did not return the expected result.")


if __name__ == '__main__':
    unittest.main()
