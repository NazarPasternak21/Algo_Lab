import unittest

from main import BinaryTree, branchSums


class TestBranchSums(unittest.TestCase):
    def test_branch_sums(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        result = branchSums(root)
        self.assertEqual(result, 24)


if __name__ == '__main__':
    unittest.main()
