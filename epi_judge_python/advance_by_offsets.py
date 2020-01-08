from test_framework import generic_test


def can_reach_end(nums):
    min_index = len(nums) - 1
    for i in reversed(range(len(nums))):
        if i + nums[i] >= min_index:
            min_index = i

    return min_index == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
