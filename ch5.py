def insert_substring(string, substring, start, stop):

    if not len(substring) == stop - start + 1:
        raise Exception('stop - start + 1 must be equal to the length of the substring')
    if not len(substring) < len(string):
        raise Exception('substring must be shorter than string')
    if not start < len(string) and not stop < len(string):
        raise Exception('indices start and stop must fit inside string')

    string_size = len(string)
    new_letters = []
    for i in range(string_size - stop - 1):
        new_letters.append(string[i])
    for i in range(stop - start + 1):
        new_letters.append(substring[i])
    for i in range(string_size - start, string_size):
        new_letters.append(string[i])

    new_string = ''.join(new_letters)
    return new_string

