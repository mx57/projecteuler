from projecteuler import util


def solution():
    """
    The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """

    sum_of_sqr = sum([i ** 2 for i in range(101)])
    sqr_of_sum = sum(range(101)) ** 2
    return sqr_of_sum - sum_of_sqr


if __name__ == '__main__':
    assert str(solution()) == util.get_answer(6)
