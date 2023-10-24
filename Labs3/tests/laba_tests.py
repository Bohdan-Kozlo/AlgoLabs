import unittest

from src.laba import BinaryTree, get_height, is_tree_balanced


class TestBinaryTree(unittest.TestCase):

     def test_is_tree_balanced(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(4)
        root.right.right = BinaryTree(5)

        self.assertTrue(is_tree_balanced(root))

        root.right.right.right = BinaryTree(6)
        self.assertFalse(is_tree_balanced(root))

if __name__ == '__main__':
    unittest.main()
