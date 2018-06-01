import pytest
from ch1 import (is_anagram,
                 unique,
                 remove_duplicates,
                 replace_with)


class TestUnique(object):
    def test_false(self):
        assert unique('abcdd') is False

    def test_true(self):
        assert unique('abcd') is True


class TestRemoveDuplicates(object):
    @pytest.mark.skip(reason='not implemented yet')
    def test_remove_dupes(self):
        output = remove_duplicates('stuff')
        assert output == 'stuf'


class TestAnagram(object):
    def test_wrong_lengths(self):
        output = is_anagram('racecar', 'rya')
        assert output is False

    def test_not_anagram(self):
        output = is_anagram('racecar', 'ryan')
        assert output is False

    def test_is_anagram(self):
        output = is_anagram('racecar', 'racecar')
        assert output is True


@pytest.mark.parametrize(
    "string, expected",
    [('something ', 'something%20'),
     ('stuf again over', 'stuf%20again%20over')]
)
def test_replace_with(string, expected):
    assert replace_with(string) == expected

