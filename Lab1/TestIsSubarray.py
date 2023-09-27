import unittest

from IsSubarray import is_subarray


class TestIsSubarray(unittest.TestCase):

    def test_subarray_exists(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4]
        self.assertTrue(is_subarray(nums1, nums2))

    def test_subarray_not_exists(self):
        nums1 = [4, 2]
        nums2 = [1, 2, 3, 4]
        self.assertFalse(is_subarray(nums1, nums2))

    def test_empty_array(self):
        nums1 = []
        nums2 = [1, 2, 3, 4]
        self.assertTrue(is_subarray(nums1, nums2))

    def test_subarray_with_duplicates(self):
        nums1 = [1, 3, 3]
        nums2 = [1, 2, 3, 4, 5, 3, 3]
        self.assertTrue(is_subarray(nums1, nums2))

if __name__ == '__main__':
    unittest.main()