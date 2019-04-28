class SimpleMaths():
    '''
    A simple class to allow calculations to be performed on an integer.
    '''
    def __init__(self, number):
        if type(number) != int:
            raise TypeError('{} is a {} not an integer'.format(number, type(number)))
        self.number = number

    def square(self):
        return self.number ** 2

    def _factorial(self, value):
        if value == 0:
            return 1
        elif value > 0:
            return value * self._factorial(value - 1)
        else:
            raise Exception('Factorial can only be calculated for positive integers.')

    def factorial(self):
        return self._factorial(self.number)

    def power(self, power=3):
        return self.number ** power

    def odd_or_even(self):
        '''
        Note that this code assumes that 0 is even.
        '''
        if (self.number % 2) == 0:
            return 'Even'
        elif (self.number % 2) == 1:
            return 'Odd'

    def square_root(self):
        return self.number ** (0.5)
