import pytest

from ch5 import insert_substring


@pytest.mark.parametrize(
    "n, m, start, stop, expected",
    [
        ('10000000000', '10101', 2, 6, '10001010100'),
        ('10000000000', '10101', 1, 6, 'raise'),
        ('1000', '10100', 2, 6, 'raise'),
    ]
)
def test_insert_substring(n, m, start, stop, expected):
    if expected == 'raise':
        with pytest.raises(Exception):
            insert_substring(n, m, start, stop)
    else:
        output = insert_substring(n, m, start, stop)
        assert output == expected

