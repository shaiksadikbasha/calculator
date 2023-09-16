import math
import random

class Calculator:
    def __init__(self):
        print("Welcome to Basha's Calculator!")
        print("I hope you enjoy using this calculator :)")

    def display_options(self):
        print("\nOptions")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'more' to see a list of more operations available")
        print("Enter 'quit' to end the program")

    def add_numbers(self):
        try:
            num1 = float(input("Enter the first number: \n"))
            num2 = float(input("Enter the second number: "))
            result = str(num1 + num2)
            print("\nThe answer is " + result)
        except (ValueError, TypeError):
            print("Error occurred")

    def subtract_numbers(self):
        try:
            num1 = float(input("Enter the first number: \n"))
            num2 = float(input("Enter the second number: "))
            result = str(num1 - num2)
            print("\nThe answer is " + result)
        except (ValueError, TypeError):
            print("Error occurred")

    def multiply_numbers(self):
        try:
            num1 = float(input("Enter the first number: \n"))
            num2 = float(input("Enter the second number: "))
            result = str(num1 * num2)
            print("\nThe answer is " + result)
        except (ValueError, TypeError):
            print("Error occurred")

    def divide_numbers(self):
        try:
            num1 = float(input("Enter the first number: \n"))
            num2 = float(input("Enter the second number: "))
            result = str(num1 / num2)
            print("\nThe answer is " + result)
        except ZeroDivisionError:
            print("An error has occurred due to zero division")
        except (ValueError, TypeError):
            print("Error occurred")

    def powers(self):
        try:
            num1 = float(input("Enter the base number: \n"))
            num2 = float(input("Enter the exponent: "))
            result = str(num1 ** num2)
            print("\nThe answer is " + result)
        except (ValueError, TypeError):
            print("Error occurred")

    def calculate_square_root(self):
        try:
            num = float(input("Enter a number: "))
            result = str(math.sqrt(num))
            print("\nThe answer is " + result)
        except (ValueError, TypeError):
            print("Error occurred")

    def calculate_percentage(self):
        try:
            num = float(input("Enter a number: "))
            result = str(num / 100)
            print("\nThe answer is " + result)
        except (ValueError, TypeError):
            print("Error occurred")
        
    def calculate_factorial(self):
        try:
            num = int(input("Enter a number: "))
            result = math.factorial(num)
            print("\nThe answer is " + str(result))
        except (ValueError, TypeError):
            print("Error occurred")

    def calculate_sine(self):
        try:
            angle_degrees = float(input("Enter an angle in degrees: "))
            angle_radians = math.radians(angle_degrees)
            result = math.sin(angle_radians)
            print("\nThe answer is " + str(result))
        except (ValueError, TypeError):
            print("Error occurred")

    def calculate_cosine(self):
        try:
            angle_degrees = float(input("Enter an angle in degrees: "))
            angle_radians = math.radians(angle_degrees)
            result = math.cos(angle_radians)
            print("\nThe answer is " + str(result))
        except (ValueError, TypeError):
            print("Error occurred")

    def calculate_tangent(self):
        try:
            angle_degrees = float(input("Enter an angle in degrees: "))
            angle_radians = math.radians(angle_degrees)
            result = math.tan(angle_radians)
            print("\nThe answer is " + str(result))
        except (ValueError, TypeError):
            print("Error occurred")

    def generate_random_number(self):
        result = str(random.random())
        print("\nThe answer is " + result)

    def generate_random_integer(self):
        try:
            num1 = int(input("Enter the first number: \n"))
            num2 = int(input("Enter the second number: "))
            result = str(random.randint(num1, num2))
            print("\nThe answer is " + result)
        except (ValueError, TypeError):
            print("An error occurred")

    def run_calculator(self):
        self.display_options()

        while True:
            user_input = input("\nPlease input your command: \n")

            if user_input == "options":
                self.display_options()

            elif user_input == "more":
                print("\nList of more operations")
                print("Enter 'powers' to raise a number to the power of another")
                print("Enter 'sqrt' to find the square root of a number")
                print("Enter 'percent' to calculate the percentage of a number")
                print("Enter 'factorial' to calculate the factorial of a number")
                print("Enter 'pi' to return the value of pi")
                print("Enter 'e' to return the value of e")
                print("Enter 'sin' to find the sine of a number")
                print("Enter 'cos' to find the cosine of a number")
                print("Enter 'tan' to find the tangent of a number")
                print("Enter 'rand' to return a random number between 0 and 1")
                print("Enter 'randint' to return a random number between two numbers")

            elif user_input == "quit":
                print("\nThank you for using this calculator!")
                break

            elif user_input == "add":
                self.add_numbers()

            elif user_input == "subtract":
                self.subtract_numbers()

            elif user_input == "multiply":
                self.multiply_numbers()

            elif user_input == "divide":
                self.divide_numbers()

            elif user_input == "powers":
                self.powers()

            elif user_input == "sqrt":
                self.calculate_square_root()

            elif user_input == "percent":
                self.calculate_percentage()

            elif user_input == "factorial":
                self.calculate_factorial()

            elif user_input == "pi":
                result = str(math.pi)
                print("\nThe answer is " + result)

            elif user_input == "e":
                result = str(math.e)
                print("\nThe answer is " + result)

            elif user_input == "sin":
                self.calculate_sine()

            elif user_input == "cos":
                self.calculate_cosine()

            elif user_input == "tan":
                self.calculate_tangent()

            elif user_input == "rand":
                self.generate_random_number()

            elif user_input == "randint":
                self.generate_random_integer()

            else:
                print("Unknown input")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_calculator()
