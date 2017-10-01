from projecteuler import utilities as utl


def solution():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    return sum([x for x in range(1000) if not x % 3 or not x % 5])


if __name__ == '__main__':
    assert str(solution()) == utl.get_answer(1)
