import math


def addition(variables):
    result = variables[0]
    for variable in variables[1:]:
        result += variable
    return result


def subtract(variables):
    result = variables[0]
    for variable in variables[1:]:
        result -= variable
    return result


def multiply(variables):
    result = variables[0]
    for variable in variables[1:]:
        result *= variable
    return result


def divide(variables):
    result = variables[0]
    for variable in variables[1:]:
        result /= variable
    return result


def exponent(variables):
    return variables[0] ** 2


def square(variables):
    return math.sqrt(variables[0])


def cos(variables):
    return math.cos(variables[0])


def sin(variables):
    return math.sin(variables[0])


def tan(variables):
    return math.tan(variables[0])


def cot(variables):
    return math.cos(variables[0]) / math.sin(variables[0])
