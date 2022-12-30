import operations


def greetings():
    print("Hi, I'm Calculator.\n")


def print_operations_list():
    print("At this moment you can: \n ")
    operations_dictionary = operations.operations_dictionary

    for operation in operations_dictionary:
        operation_name = operations_dictionary[operation]['operation_name']
        operation_key = operations_dictionary[operation]['operation_key']
        print(f"{operation_name} - for this operation input {operation_key}, and press Enter")


def input_operation():
    return input('Write what do you want to do? \n')


def input_numbers():
    return input('You can write only numbers, if you try write a letter or symbol its provide an error\n'
                 'Write number... \n')


def get_result(result):
    print(f"Your result is: {result}")
