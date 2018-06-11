import ch8


def test_fib():
    assert ch8.fib(6) == 8


def test_fib_const():
    assert ch8.fib_iterative(6) == 8
