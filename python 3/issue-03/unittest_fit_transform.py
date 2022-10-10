import unittest
from one_hot_encoder import fit_transform


class testFitTransform(unittest.TestCase):
    def test_example(self):
        actual = ['Moscow', 'New York', 'Moscow', 'London']
        excepted = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(actual), excepted)

    def test_not_in(self):
        actual = ['Moscow', 'New York', 'Moscow', 'London']
        unexpected = ('Moscow', [1, 0, 0])
        self.assertNotIn(unexpected, fit_transform(actual))

    def test_TypeError(self):
        self.assertRaises(TypeError, lambda: fit_transform())

    def test_in(self):
        actual = ['Moscow', 'New York', 'Moscow', 'London']
        unexpected = ('Moscow', [0, 0, 1])
        self.assertIn(unexpected, fit_transform(actual))
