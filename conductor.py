import dialog
import operations

numbers_list = []
operation_data_list = {}


def run():
    dialog.print_operations_list()
    get_operation()
    processing()


def processing():
    result = dialog.get_result
    get_variables()
    operation_function = operation_data_list['operation_function']
    result(operation_function(numbers_list))


def get_operation():
    operations_dictionary = operations.operations_dictionary
    operation = dialog.input_operation()
    for operation_dictionary in operations_dictionary:
        operation_key = operations_dictionary[operation_dictionary]['operation_key']
        if operation == operation_key:
            operation_data_list['operation_rule'] = operations_dictionary[operation_dictionary]['operation_rule']
            operation_data_list['operation_function'] = operations_dictionary[operation_dictionary]['operation']


def get_variables():
    operation_rule = operation_data_list['operation_rule']
    print(operation_rule)

    if len(numbers_list) >= 2:
        print('For getting result just pres ENTER')

    number = dialog.input_numbers()

    if number == '0':
        print("You can't write zero, because ist provide an error")
        return get_variables()
    elif number != '':
        numbers_list.append(float(number))
        return get_variables()
    elif number == '':
        if operation_rule == operations.VARIABLES_OPERATION_RULE and len(numbers_list) <= 1:
            print('Invalid numbers. You must write minimum 2 numbers')
            get_variables()
        elif operation_rule == operations.VARIABLE_OPERATION_RULE or (
                operation_rule == operations.VARIABLES_OPERATION_RULE and len(numbers_list) >= 2):
            return
