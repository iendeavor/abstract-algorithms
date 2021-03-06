import unittest

from lib.array import (
    n_sum,
)


class TestNSum(unittest.TestCase):

    def test_n_sum(self):
        self.assertEqual(n_sum(2, [-3, 5, 2, 3, 8, -9], 6), [])  # noqa: E501
        self.assertEqual(n_sum(3, [-5, -4, -3, -2, -1, 0, 1, 2, 3], 0), sorted([[-5, 2, 3], [-2, 0, 2], [-4, 1, 3], [-3, 1, 2], [-1, 0, 1], [-2, -1, 3], [-3, 0, 3]]))  # noqa: E501
        self.assertEqual(n_sum(3, [-1, 0, 1, 2, -1, -4], 0), sorted([[-1, -1, 2], [-1, 0, 1]]))  # noqa: E501
        self.assertEqual(n_sum(4, [1, 0, -1, 0, -2, 2], 0), sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]))  # noqa: E501
        self.assertEqual(n_sum(4, [7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 6, 4, -3, -2], 10), sorted([[-6, 2, 7, 7], [-6, 3, 6, 7], [-6, 4, 5, 7], [-6, 4, 6, 6], [-5, 1, 7, 7], [-5, 2, 6, 7], [-5, 3, 5, 7], [-5, 3, 6, 6], [-5, 4, 4, 7], [-5, 4, 5, 6], [-4, 0, 7, 7], [-4, 1, 6, 7], [-4, 2, 5, 7], [-4, 2, 6, 6], [-4, 3, 4, 7], [-4, 3, 5, 6], [-4, 4, 4, 6], [-3, -1, 7, 7], [-3, 0, 6, 7], [-3, 1, 5, 7], [-3, 1, 6, 6], [-3, 2, 4, 7], [-3, 2, 5, 6], [-3, 3, 4, 6], [-3, 4, 4, 5], [-2, -2, 7, 7], [-2, -1, 6, 7], [-2, 0, 5, 7], [-2, 0, 6, 6], [-2, 1, 4, 7], [-2, 1, 5, 6], [-2, 2, 3, 7], [-2, 2, 4, 6], [-2, 3, 4, 5], [-1, 0, 4, 7], [-1, 0, 5, 6], [-1, 1, 3, 7], [-1, 1, 4, 6], [-1, 2, 3, 6], [-1, 2, 4, 5], [-1, 3, 4, 4], [0, 1, 2, 7], [0, 1, 3, 6], [0, 1, 4, 5], [0, 2, 3, 5], [0, 2, 4, 4], [1, 2, 3, 4]]))  # noqa: E501

        self.assertEqual(n_sum(2, [[-3, 0], [-2, 1], [2, 2], [3, 3], [8, 4], [-9, 5]], 0,  # noqa: E501
                               sum_closure=lambda a, b: a[0] + b[0]),  # noqa: E501
                         [[[-3, 0], [3, 3]], [[-2, 1], [2, 2]]])  # noqa: E501
        self.assertEqual(n_sum(2, [[-3, 0], [-2, 1], [2, 2], [3, 3], [8, 4], [-9, 5]], [0, 3],  # noqa: E501
                               sum_closure=lambda a, b: [a[0] + b[0], a[1] + b[1]],  # noqa: E501
                               same_closure=lambda a, b: a[0] == b[0] and a[1] == b[1]),  # noqa: E501
                         [[[-3, 0], [3, 3]], [[-2, 1], [2, 2]]])  # noqa: E501
        self.assertEqual(n_sum(2, [[-3, 0], [-2, 1], [2, 2], [3, 3], [8, 4], [-9, 5]], -5,  # noqa: E501
                               sum_closure=lambda a, b: [a[0] + b[1], a[1] + b[0]],  # noqa: E501
                               compare_closure=lambda a, b: -1 if a[0] < b else 1 if a[0] > b else 0),  # noqa: E501
                         [[[-9, 5], [8, 4]]])  # noqa: E501
