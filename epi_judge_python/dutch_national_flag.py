import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # TODO - you fill in here.
    # front = 0
    # end = int(len(A) - 1)
    # pivot = A[pivot_index]

    # # for i in range(len(A)):
    # while front < end:
    #     if A[front] <= pivot & pivot_index > front:
    #         front += 1
    #     elif A[front] < pivot & pivot_index <= front:
    #         tmp = A[front]
    #         A[front] = A[pivot_index]
    #         A[pivot_index] = tmp
    #         pivot_index = front
    #         front += 1
    #     elif A[front] > pivot:
    #         tmp = A[front]
    #         A[front] = A[end]
    #         A[end] = tmp
    #         end -= 1
    #     # elif A[front] == pivot:
        #     front += 1
    less = []
    more = []
    equal = []
    for i in range(len(A)):
        if A[i] < A[pivot_index]:
            less.append(A[i])
        elif A[i] > A[pivot_index]:
            more.append(A[i])
        else:
            equal.append(A[i])

    for i in range(len(less)):
        A[i] = less[i]
    for j in range(len(equal)):
        A[len(less) + j] = equal[j]
    for k in range(len(more)):
        A[len(less) + len(equal) + k] = more[k]

    return A


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
