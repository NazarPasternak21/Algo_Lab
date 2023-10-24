class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    def helper(node, is_left):
        if node is None:
            return 0
        if node.left is None and node.right is None and is_left:
            return node.value
        left_sum = helper(node.left, True)
        right_sum = helper(node.right, False)
        return left_sum + right_sum

    return helper(root, False)


root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

result = branchSums(root)
print(result)
