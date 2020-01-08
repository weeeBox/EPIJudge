from test_framework import generic_test


def multiply(num1, num2):
    def sign(val):
        return 1 if val >= 0 else -1

    s = sign(num1[0]) * sign(num2[0])
    i = len(num2) - 1
    k = 0
    res = [0] * (len(num1) + len(num2))
    carry = 0
    while i >= 0:
        d1 = abs(num2[i])
        j = len(num1) - 1
        t = k
        while j >= 0 or carry > 0:
            prod = (d1 * abs(num1[j])) if j >= 0 else 0
            temp = res[t] + prod + carry
            res[t] = temp % 10
            carry = temp // 10
            j -= 1
            t += 1
        k += 1
        i -= 1

    while len(res) > 1 and res[-1] == 0:
        res.pop()

    res.reverse()
    res[0] *= s
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
