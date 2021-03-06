import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(nums):
    """
        j
    12345455
           i
    """

    i = j = 0
    while i < len(nums):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

        i += 1

    return j + 1


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
