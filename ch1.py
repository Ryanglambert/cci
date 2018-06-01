import numpy as np


def unique(chars: str):
    length = len(chars)
    if not len(set(list(chars))) == length:
        return False
    return True


def remove_duplicates(chars: str):
    raise NotImplemented


def is_anagram(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1) // 2 + 1):
        if not str1[i] == str2[i]:
            return False
    return True


def replace_with(string: str, old=' ', new='%20'):
    new_letters = []
    for letter in string:
        if letter == old:
            new_letters.append(new)
        else:
            new_letters.append(letter)
    new_string = ''.join(new_letters)
    return new_string


def rotate_img_90(img: np.array):
    raise NotImplemented


def zerofy_rows(matrix: np.array):
    raise NotImplemented

