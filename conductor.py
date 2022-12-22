import dialog
import operations

numbers_list = []


def run():
    dialog.print_operations_list()
    processing()


def processing():
    operation = dialog.get_operation()
    result = dialog.get_result
    if operation == '1':
        result(operations.addition(get_many_variables()))
    elif operation == '2':
        result(operations.subtract(get_many_variables()))
    elif operation == '3':
        result(operations.multiply(get_many_variables()))
    elif operation == '4':
        result(operations.divide(get_many_variables()))
    elif operation == '5':
        result(operations.square(get_one_variable()))
    elif operation == '6':
        result(operations.sqrt(get_one_variable()))
    elif operation == '7':
        result(operations.cos(get_one_variable()))
    elif operation == '8':
        result(operations.sin(get_one_variable()))
    elif operation == '9':
        result(operations.tan(get_one_variable()))
    elif operation == '0':
        result(operations.cot(get_one_variable()))
    else:
        print('Invalid operation. Please try again!')
        run()


def get_one_variable():
    print("For this operation, You must write only 1 number")
    number = dialog.input_numbers()
    if number == '0':
        print("You can't write zero, because ist provide an error")
        return get_one_variable()
    elif number != '':
        numbers_list.append(int(number))
        return numbers_list
    else:
        print("Invalid number")
        get_one_variable()


def get_many_variables():
    print("For this operation, You must write minimum 2 numbers")
    number = dialog.input_numbers()
    if number == '0':
        print("You can't write zero, because ist provide an error")
        return get_many_variables()
    elif number != '':
        numbers_list.append(int(number))
        return get_many_variables()
    else:
        if len(numbers_list) <= 1:
            print('Invalid numbers. You must write minimum 2 numbers')
            return get_many_variables()
        else:
            return numbers_list
