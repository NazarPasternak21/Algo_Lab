import unittest
from src.main import topological_sort


class TestTopologicalSort(unittest.TestCase):
    def test_topological_sort(self):
        graph = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['d'],
            'd': []
        }

        expected_result = ['d', 'b', 'c', 'a']

        result = topological_sort(graph)
        print(f"Expected Result: {expected_result}")
        print(f"Actual Result: {result}")
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
