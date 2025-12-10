def show_menu():
    print("\n====== PROFESSIONAL CALCULATOR ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Floor Division (//)")
    print("0. Exit")
    print("=====================================")

def calculate():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Thank you for using the calculator! Goodbye.")
            break

        if choice not in ["1","2","3","4","5","6","7"]:
            print("❌ Invalid choice! Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Numbers only.")
            continue

        if choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            if num2 == 0:
                print("❌ Error: Division by zero not allowed!")
                continue
            result = num1 / num2
        elif choice == "5":
            result = num1 % num2
        elif choice == "6":
            result = num1 ** num2
        elif choice == "7":
            if num2 == 0:
                print("❌ Error: Division by zero not allowed!")
                continue
            result = num1 // num2

        print(f"✅ Result: {result}")

# Run calculator
calculate()
