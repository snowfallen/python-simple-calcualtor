import dialog
import operations


class Conductor:
    variables_list = []

    dialog = dialog.Dialog
    operations = operations.Operations

    def run(self):
        self.dialog.print_operations_list()
        self.processing()

    def processing(self):
        operation = self.dialog.get_operation()
        result = self.dialog.get_result
        if operation == '1':
            result(self.operations.addition(self.get_many_variables()))
        elif operation == '2':
            result(self.operations.subtract(self.get_many_variables()))
        elif operation == '3':
            result(self.operations.multiply(self.get_many_variables()))
        elif operation == '4':
            result(self.operations.divide(self.get_many_variables()))
        elif operation == '5':
            result(self.operations.exponent(self.get_one_variable()))
        elif operation == '6':
            result(self.operations.square(self.get_one_variable()))
        elif operation == '7':
            result(self.operations.cos(self.get_one_variable()))
        elif operation == '8':
            result(self.operations.sin(self.get_one_variable()))
        elif operation == '9':
            result(self.operations.tan(self.get_one_variable()))
        elif operation == '0':
            result(self.operations.cot(self.get_one_variable()))
        else:
            print('Invalid operation. Please try again!')
            self.run()

    def get_one_variable(self):
        variable = self.dialog.get_variables()
        if variable == '0':
            print("You can't write zero, because ist provide an error")
            return self.get_one_variable()
        elif variable != '':
            self.variables_list.append(int(variable))
            return self.variables_list
        else:
            print("Invalid number")
            self.get_one_variable()

    def get_many_variables(self):
        variable = self.dialog.get_variables()
        if variable == '0':
            print("You can't write zero, because ist provide an error")
            return self.get_many_variables()
        elif variable != '':
            self.variables_list.append(int(variable))
            return self.get_many_variables()
        else:
            if len(self.variables_list) <= 1:
                print('Invalid numbers. You must write minimum 2 numbers')
                return self.get_many_variables()
            else:
                return self.variables_list


