#!/usr/bin/env python3
"""
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

def fibonacci_numbers():
    first, second = 0, 1
    ls_second = []

    while second < 4000000:
        first, second = second, first + second
        if not second % 2: ls_second.append(second)
    return sum(ls_second)
