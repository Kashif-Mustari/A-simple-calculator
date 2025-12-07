def calculator():
    print("\n===== Simple Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == "5":
        print("Exiting calculator... Goodbye!")
        return False   # Stop loop

    # Validate numeric choice
    if choice not in ["1", "2", "3", "4"]:
        print("⚠ Invalid choice! Please try again.")
        return True

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("⚠ Error: Please enter valid numbers!")
        return True

    if choice == "1":
        print("➡ Result:", num1 + num2)

    elif choice == "2":
        print("➡ Result:", num1 - num2)

    elif choice == "3":
        print("➡ Result:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("➡ Result:", num1 / num2)
        else:
            print("❌ Error: Division by zero is not allowed!")

    return True  # Continue loop


# Run calculator in a loop
run = True
while run:
    run = calculator()
