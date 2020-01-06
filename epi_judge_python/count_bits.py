from test_framework import generic_test


def count_bits(x):
    count = 0
    while x != 0:
        x = x & (x - 1)
        count += 1
    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
