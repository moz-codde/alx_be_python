def perform_operation(num1:float, num2:float, operation:str):
    def add(num1, num2):
        return num1 + num2
    def subtract(num1, num2):
        return num1 - num2
    def multiply(num1, num2):
        return num1 * num2
    def divide(num1, num2):
        if num2 == 0:
            return "Division by Zero not allowed"
        else:
            return num1 / num2
    operations = {'add': add, 'subtract': subtract, 'multiply': multiply, 'divide': divide}
    return operations[operation](num1, num2)
