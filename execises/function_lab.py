# ## Lab: functions
# * Write a function __`calculate`__ which is passed two operands and an operator
# and returns the calculated result, e.g., __`calculate(2, 4, '+')`__ would return 6


def calculate(operand1, operand2, operator):
    '''
    calculate accepts two operands and an operator
    and returns the calculated result.
    e.g., calculate(2, 4, '+') would return 6
    '''
    calc_functions = {}
    calc_functions['+'] = lambda a, b: a + b
    calc_functions['-'] = lambda a, b: a - b
    calc_functions['*'] = lambda a, b: a * b
    calc_functions['/'] = lambda a, b: a / b
    if not (operator in calc_functions):
        raise ValueError('unknown operator:' + operator)
    return calc_functions[operator](operand1, operand2)


# * Write a function which takes an integer as a parameter, and sums up its digits.
# If the resulting sum contains more than 1 digit, the function should sum the digits again,
# e.g., __`sumdigits(1235)`__ should compute the sum of 1, 2, 3, and 5 (11),
# then compute the sum of 1 and 1, returning 2.
def sumdigits(num):
    '''
    takes an integer as a parameter, and sums up its digits.
    If the resulting sum contains more than 1 digit, the function should sum the digits again,
    e.g., __`sumdigits(1235)`__ should compute the sum of 1, 2, 3, and 5 (11),
    then compute the sum of 1 and 1, returning 2.
    '''
    if not isinstance(num, int):
        raise TypeError('Expect an integer, but get {}'.format(num))
    if num < 0:
        raise ValueError(
            'Expecting a non negitive number, but get:{}'.format(num))
    if 0 <= num <= 9:
        return num

    s = 0
    while num > 0:
        num, last_digit = divmod(num, 10)
        s += last_digit

    return sumdigits(s)


# * Write a function which takes a number as a parameter and returns a string
# version  of the number with commas representing thousands,
# e.g., __`add_commas(12345)`__ would return "12,345"


# write a function called product which accepts a variable number of arguments
# and returns the product of all of its args. With no args, product() should return 1
# >>> product(3, 5)
# 15
# >>> product(1, 2, 3)
# 6
# >>> product(63, 12, 3, 0, 9)
# 0
# >>> product()
# 1

def product(*numbers):
    '''
    product accepts a variable number of arguments and returns the product of all of its args. With no args, product() should return 1
    >>> product(3, 5)==15
    >>> product(1, 2, 3)==6
    >>> product(63, 12, 3, 0, 9)==0
    >>> product()==1
    '''
    for arg in numbers:
        assert isinstance(arg, int) or isinstance(
            arg, float), "expect all args to be int or float"
    p = 1
    for n in numbers:
        p *= n
    return p


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
    print 'Calculate'
    test(calculate(1, 2, '+'), 3)
    test(calculate(5, 6, '-'), -1)
    test(calculate(3.0, -2.0, '*'), -6.0)
    test(calculate(3.0, -2.0, '/'), -1.5)

    try:
        test(calculate(3.0, -2.0, '@#'), ValueError('unknown operator:' + '@#'))
    except ValueError as e:
        print e.message

    print
    print 'sumdigits'
    test(sumdigits(0), 0)
    test(sumdigits(7), 7)
    test(sumdigits(10), 1)
    test(sumdigits(99), 9)
    test(sumdigits(12345), 6)

    try:
        test(sumdigits(-93838), -1)
    except ValueError as e:
        print(e.message)

    try:
        test(sumdigits('badNumber'), -1)
    except TypeError as e:
        print e.message

    print
    print 'product'
    test(product(), 1)
    test(product(0), 0)
    test(product(7), 7)
    test(product(-2, 10), -20)
    test(product(2.0, 0, 1.5), 0)
    test(product(2.0, 3, 1.5), 9.0)

    try:
        test(product('bad'), -1)
    except AssertionError as e:
        print('Assertion Failed:' + e.message)


if __name__ == '__main__':
    main()
