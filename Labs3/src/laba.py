class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_height(node):
    if node is None:
        return -1
    else:
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        return max(left_height, right_height) + 1


def is_tree_balanced(node: BinaryTree):
    if node is None:
        return True

    if abs(get_height(node.left) - get_height(node.right)) <= 1:
        return True
    else:
        return False


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(3)
root.right = BinaryTree(4)

print(get_height(root.right))

print(is_tree_balanced(root))
