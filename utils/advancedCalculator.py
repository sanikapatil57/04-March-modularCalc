# Advanced calculator using inheritance
from utils.calculator import Calculator

class AdvancedCalculator(Calculator):

    def power(self):
        return self.first_number ** self.second_number

    def square_root(self):
        if self.first_number < 0:
            return "Error: Cannot calculate square root of a negative number."
        return self.first_number ** 0.5