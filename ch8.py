def fib(n):
    'fully recursive'
    if not n >= 0:
        raise Exception("number must be greater than or equal to 0")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # the fib for n - 2 could be avoided by passing in a second argument to this function
        # containing the last value
        # then this could be treated like a series without calculating the fib
        # for each 
        return fib(n - 1) + fib(n - 2)


def fib_iterative(n):
    'iterative, but does no extra computation of fib each time'
    if not n >= 0:
        raise Exception("number must be greater than or equal to 0")
    if n == 0:
        return 0
    if n == 1:
        return 1

    last = 0
    current = 1
    for i in range(2, n + 1):
        # one add operation is done at each increment instead of two
        # as seen in the recursive function above
        new = last + current
        last = current
        current = new

    return current

