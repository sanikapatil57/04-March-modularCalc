from utils.advancedCalculator import AdvancedCalculator
def main():

    while True:

        print("\nCalculator")
        print("Operations: +  -  *  /  ^  sqrt")

        choice = input("Q => Quit or press ENTER to continue: ")

        if choice.upper() == 'Q':
            print("Exiting the calculator. Goodbye!")
            break

        first_number = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /, ^, sqrt): ")
        operation = operation.lower()
        if operation != "sqrt":
            second_number = float(input("Enter the second number: "))
        else:
            second_number = None

        calculator = AdvancedCalculator(first_number, operation, second_number)

        if calculator.operation == '+':
            result = calculator.add()

        elif calculator.operation == '-':
            result = calculator.subtract()

        elif calculator.operation == '*':
            result = calculator.multiply()

        elif calculator.operation == '/':
            result = calculator.divide()
        
        elif calculator.operation == '^':
            result = calculator.power()

        elif calculator.operation == 'sqrt':
            result = calculator.square_root()

        else:
            result = "Error: Invalid operation."

        print(f"Result: {result}")


if __name__ == "__main__":
    main()