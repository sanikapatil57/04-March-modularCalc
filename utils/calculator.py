class Calculator:

    def __init__(self, first_number, operation, second_number):
        self.first_number = first_number
        self.operation = operation
        self.second_number = second_number

    def add(self):
        return self.first_number + self.second_number

    def subtract(self):
        return self.first_number - self.second_number

    def multiply(self):
        return self.first_number * self.second_number

    def divide(self):
        if self.second_number == 0:
            return "Error: Division by zero is not allowed."
        return self.first_number / self.second_number