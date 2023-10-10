import unittest


def find_triplet_sum(arr, P):
    n = len(arr)

    arr.sort()

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == P:
                return True
            elif current_sum < P:
                left += 1
            else:
                right -= 1
    return False


class TestFindTripletSum(unittest.TestCase):

    def test_positive_case(self):
        arr = [1, 2, 3, 4, 5, 6]
        P = 8
        result = find_triplet_sum(arr, P)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
