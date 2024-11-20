# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error: division by zero!"
    return x / y

# Basic function of the calculator
def calculator():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # User selection input
    choice = input("Enter the transaction number (1/2/3/4): ")

    # Input numbers
    num1 = float(input("Type in the first number: "))
    num2 = float(input("Type in the second number: "))

    # Call the corresponding function
    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid input!")

# Run the calculator
if __name__ == "__main__":
    calculator()
