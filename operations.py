import math

VARIABLE_OPERATION_RULE = 'For this operation, You must write only 1 number'
VARIABLES_OPERATION_RULE = 'For this operation, You must write minimum 2 number'


def addition(*numbers):
    for number in numbers:
        return sum(number)


def subtract(*numbers):
    result = numbers[0][0]
    for number in numbers[0][1:]:
        result -= number
    return result


def multiply(*numbers):
    result = numbers[0][0]
    for number in numbers[0][1:]:
        result *= number
    return result


def divide(*numbers):
    result = numbers[0][0]
    for number in numbers[0][1:]:
        result /= number
    return result


def square(*numbers):
    return numbers[0][0] ** numbers[0][0]


def square_root(*numbers):
    return math.sqrt(numbers[0][0])


def cos(*numbers):
    return math.cos(numbers[0][0])


def sin(*numbers):
    return math.sin(numbers[0][0])


def tan(*numbers):
    return math.tan(numbers[0][0])


def cot(*numbers):
    return math.cos(numbers[0][0]) / math.sin(numbers[0][0])


operations_dictionary = {
    'addition':
        {'operation_name': 'Addition',
         'operation_key': '1',
         'operation_rule': VARIABLES_OPERATION_RULE,
         'operation': addition},
    'subtract':
        {'operation_name': 'Subtract',
         'operation_key': '2',
         'operation_rule': VARIABLES_OPERATION_RULE,
         'operation': subtract},
    'multiply':
        {'operation_name': 'Multiply',
         'operation_key': '3',
         'operation_rule': VARIABLES_OPERATION_RULE,
         'operation': multiply},
    'divide':
        {'operation_name': 'Divide',
         'operation_key': '4',
         'operation_rule': f"{VARIABLES_OPERATION_RULE}. And you can't divide 0",
         'operation': divide},
    'square':
        {'operation_name': 'Square',
         'operation_key': '5',
         'operation_rule': VARIABLE_OPERATION_RULE,
         'operation': square},
    'square_root':
        {'operation_name': 'Square root',
         'operation_key': '6',
         'operation_rule': VARIABLE_OPERATION_RULE,
         'operation': square_root},
    'cos':
        {'operation_name': 'Cos',
         'operation_key': '7',
         'operation_rule': VARIABLE_OPERATION_RULE,
         'operation': cos},
    'sin':
        {'operation_name': 'Sin',
         'operation_key': '8',
         'operation_rule': VARIABLE_OPERATION_RULE,
         'operation': sin},
    'tan':
        {'operation_name': 'Tan',
         'operation_key': '9',
         'operation_rule': VARIABLE_OPERATION_RULE,
         'operation': tan},
    'cot':
        {'operation_name': 'Cot',
         'operation_key': '0',
         'operation_rule': VARIABLE_OPERATION_RULE,
         'operation': cot}
}
