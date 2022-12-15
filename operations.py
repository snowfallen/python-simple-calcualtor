import math


class Operations:
    @staticmethod
    def addition(variables):
        result = variables[0]
        for variable in variables[1:]:
            result += variable
        return result

    @staticmethod
    def subtract(variables):
        result = variables[0]
        for variable in variables[1:]:
            result -= variable
        return result

    @staticmethod
    def multiply(variables):
        result = variables[0]
        for variable in variables[1:]:
            result *= variable
        return result

    @staticmethod
    def divide(variables):
        result = variables[0]
        for variable in variables[1:]:
            result /= variable
        return result

    @staticmethod
    def exponent(variables):
        return variables[0] ** 2

    @staticmethod
    def square(variables):
        return math.sqrt(variables[0])

    @staticmethod
    def cos(variables):
        return math.cos(variables[0])

    @staticmethod
    def sin(variables):
        return math.sin(variables[0])

    @staticmethod
    def tan(variables):
        return math.tan(variables[0])

    @staticmethod
    def cot(variables):
        return math.cos(variables[0]) / math.sin(variables[0])
