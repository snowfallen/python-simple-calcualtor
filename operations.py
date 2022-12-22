import math


def addition(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result += number
    return result


def subtract(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result


def multiply(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result *= number
    return result


def divide(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result /= number
    return result


def square(numbers):
    return numbers[0] ** numbers[0]


def sqrt(numbers):
    return math.sqrt(numbers[0])


def cos(numbers):
    return math.cos(numbers[0])


def sin(numbers):
    return math.sin(numbers[0])


def tan(numbers):
    return math.tan(numbers[0])


def cot(numbers):
    return math.cos(numbers[0]) / math.sin(numbers[0])
