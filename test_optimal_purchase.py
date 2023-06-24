from unittest import TestCase

from parameterized import parameterized

from optimal_purchase import optimal_purchase


class Test(TestCase):
    @parameterized.expand([
        [
            3,
            [10, 5, 7, 3, 2, 100, 6, 10, 11],
            [1, 2, 0, 1, 3, 0, 2, 0, 0],
            [0, 1, 0, 0, 2, 1, 2, 1, 0]
        ],
        [
            5,
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ],
        [
            1,
            [10, 16, 1, 144, 13, 10, 23, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ],
        [
            2,
            [10, 1, 5, 6, 7, 8, 11, 3],
            [1, 2, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 0, 0]
        ],
        [
            10,
            [10, 1, 5, 6, 7, 8, 11],
            [1, 6, 0, 0, 0, 0, 0],
            [0, 5, 4, 3, 2, 1, 0]
        ],
    ])
    def test_optimal_purchase(self, max_items, prices, expected_bought, expected_left):
        bought, left = optimal_purchase(prices, max_items)

        assert bought == expected_bought
        assert left == expected_left
