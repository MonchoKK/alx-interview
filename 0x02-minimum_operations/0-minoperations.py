#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    num_of_operation = 0
    min_num_of_operation = 2
    while n > 1:
        while n % min_num_of_operation == 0:
            num_of_operation += min_num_of_operation
            n /= min_num_of_operation
        min_num_of_operation += 1
    return num_of_operation
