# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Main function to get user input and perform calculations
def main():
    try:
        # Get user input for two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Get user choice for operation
        print("Choose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter choice (1/2/3/4): "))
        
        # Perform calculation based on user choice
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        else:
            result = "Invalid choice"
        
        # Print the result
        print("Result: ", result)
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print("An error occurred:", str(e))

# Call the main function to run the calculator
if __name__ == "__main__":
    main()