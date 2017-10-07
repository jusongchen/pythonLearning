# -*- coding: utf-8 -*-
#
# Lab: Calculator Class
# Create a class Calculator which acts like a calculator
# Your class should have methods add(self), sub(self), mult(self), div(self), pow(self), and log(self), but you can add more if you wish
# Each of the above methods (except log(self)) should take 1 or 2 arguments–for 1 argument, e.g., add(1), your method should add to the running total. For 2 arguments, your method should act on those 2 arguments to create the new running total
# e.g., add(2, 4) should produce 6, and then when followed by multiply(5), it should produce 30
# All calculations should be stored, and should be accessible to the caller via the showcalc(self) method.
# You should also have an ac(self) "all clear" method which clears the running total and the list of calculations (i.e., showcalc(self) should produce no output, or "0.0" when preceded by ac(self))

import sys


class Calculator():
    def __init__(self):
        self.value = 0.0
        self.calc = ''

    def ac(self):
        Calculator.__init__(self)

    def showcalc(self):
        print(self.calc)

    def calculate(self, operator, op1, op2=None):
        '''
        calculate accepts two operands and an operator
        and returns the calculated result.
        e.g., calculate('+',2, 4) would return 6
        '''

        import math
        calc_functions = {}
        calc_functions['+'] = lambda a, b: a + b
        calc_functions['-'] = lambda a, b: a - b
        calc_functions['*'] = lambda a, b: a * b
        calc_functions['/'] = lambda a, b: a / b
        calc_functions['**'] = lambda a, b: a ** b
        calc_functions['log'] = lambda a, b: math.log(a, b)
        if not (operator in calc_functions):
            raise ValueError('unknown operator:' + operator)

        if op2 is None and operator == 'log':
            raise ValueError('log needs two arguments')
        elif op2 is None:
            expression = '{}{}'.format(operator, op1)
        elif operator == 'log':
            expression = '{}({},{})'.format(operator, op1, op2)
        else:
            expression = '{}{}{}'.format(op1, operator, op2)

        if op2 is None:
            op2 = op1
            op1 = self.value
        try:
            value = calc_functions[operator](op1, op2)
        except:
            self.calc += '{}\t\terror:{}\n'.format(expression, sys.exc_info()[1])
        else:
            self.value = value
            self.calc += '{}\t\t\t{}\n'.format(expression, self.value)

    def add(self, op1, op2=None):
        self.calculate('+', op1, op2)

    def sub(self, op1, op2=None):
        self.calculate('-', op1, op2)

    def mult(self, op1, op2=None):
        self.calculate('*', op1, op2)

    def div(self, op1, op2=None):
        self.calculate('/', op1, op2)

    def pow(self, op1, op2=None):
        self.calculate('**', op1, op2)

    def log(self, op1, op2):
        self.calculate('log', op1, op2)


def main():
    c = Calculator()
    c.add(0)
    c.add(2, 3)
    c.add(1.0)
    c.sub(2.5)
    c.sub(4, 2.5)
    c.mult(4)
    c.mult(4, 3.0)

    c.div(2)
    c.div(2, 0)
    c.pow(2)
    c.log(100, 10)
    c.pow(2, 4)
    c.log(100, -10)
    c.log(100, 0)
    c.showcalc()
    c.ac()
    c.showcalc()


if __name__ == '__main__':
    main()
