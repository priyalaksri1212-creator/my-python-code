def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operation!")
            return

        print(f"\nResult: {num1} {op} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
while True:
    calculator()
    again = input("\nCalculate again? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break

    