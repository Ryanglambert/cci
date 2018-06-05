def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n2 - n1


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def combine_nums(op1, op2, op3, nums=(3, 1, 3, 6)):
    first = nums[0]
    number = first
    for new in nums[1:]:
        number = op1(number, new)
    return number


def try_combinations():
    combinations_yield_correct = []
    combinations = [add, subtract, multiply, divide]
    for op1 in combinations:
        for op2 in combinations:
            for op3 in combinations:
                num = combine_nums(op1, op2, op3)
                if num == 8:
                    combinations_yield_correct.append((op1, op2, op3))

    return combinations_yield_correct


