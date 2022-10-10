from one_hot_encoder import fit_transform
import pytest


def test_int_raises_type_error():
    with pytest.raises(TypeError):
        fit_transform()


def test_example():
    actual = ['Moscow', 'New York', 'Moscow', 'London']
    excepted = [('Moscow', [0, 0, 1]),
                ('New York', [0, 1, 0]),
                ('Moscow', [0, 0, 1]),
                ('London', [1, 0, 0]),
                ]
    assert fit_transform(actual) == excepted


def test_by_args():
    arg1 = 'Moscow'
    arg2 = 'London'
    arg3 = 3
    excepted = [('Moscow', [0, 0, 1]), ('London', [0, 1, 0]), (3, [1, 0, 0])]
    assert fit_transform(arg1, arg2, arg3) == excepted


def test_duplet():
    actual = ['Moscow', 'London', 'London', 'Moscow', 'Moscow']
    excepted = [('Moscow', [0, 1]),
                ('London', [1, 0]),
                ('London', [1, 0]),
                ('Moscow', [0, 1]),
                ('Moscow', [0, 1])
                ]
    assert fit_transform(actual) == excepted
