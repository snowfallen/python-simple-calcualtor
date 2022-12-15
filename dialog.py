def greetings():
    print("Hi, I'm Calculator.\n")


def print_operations_list():
    print("At this moment you can: \n "
          "Additional, write 1 \n "
          "Subtract, write 2\n "
          "Multiply, write 3\n "
          "Divide, write 4\n "
          "Exponent, write 5\n "
          "Square, write 6\n "
          "Cosines, write 7\n "
          "Sinus, write 8\n "
          "Tangents, write 9\n "
          "Cotangents, write 0\n ")


def get_operation():
    return input('Write what do you want to do? \n')


def get_variables():
    return input('Write number... \n')


def get_result(result):
    print(f"Your result is: {result}")
