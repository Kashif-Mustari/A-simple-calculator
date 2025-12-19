<<<<<<< HEAD
import math

history = []


def show_menu():
    print("\n========= SMART CALCULATOR =========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Floor Division (//)")
    print("8. Square Root (√)")
    print("9. Sin")
    print("10. Cos")
    print("11. Log")
    print("12. Show History")
    print("13. Clear History")
    print("0. Exit")
    print("===================================")


def calculator():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            print("👋 Calculator closed. Goodbye!")
            break

        # History
        if choice == "12":
            if not history:
                print("📂 No history available.")
            else:
                print("\n📜 Calculation History:")
                for h in history:
                    print("➡", h)
            continue

        if choice == "13":
            history.clear()
            print("🗑 History cleared!")
            continue

        try:
            # Single number operations
            if choice in ["8", "9", "10", "11"]:
                num = float(input("Enter number: "))

                if choice == "8":
                    result = math.sqrt(num)
                    expression = f"√{num} = {result}"

                elif choice == "9":
                    result = math.sin(math.radians(num))
                    expression = f"sin({num}) = {result}"

                elif choice == "10":
                    result = math.cos(math.radians(num))
                    expression = f"cos({num}) = {result}"

                elif choice == "11":
                    result = math.log10(num)
                    expression = f"log({num}) = {result}"

            # Two number operations
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = num1 + num2
                    expression = f"{num1} + {num2} = {result}"

                elif choice == "2":
                    result = num1 - num2
                    expression = f"{num1} - {num2} = {result}"

                elif choice == "3":
                    result = num1 * num2
                    expression = f"{num1} * {num2} = {result}"

                elif choice == "4":
                    if num2 == 0:
                        print("❌ Division by zero!")
                        continue
                    result = num1 / num2
                    expression = f"{num1} / {num2} = {result}"

                elif choice == "5":
                    if num2 == 0:
                        print("❌ Modulus by zero!")
                        continue
                    result = num1 % num2
                    expression = f"{num1} % {num2} = {result}"

                elif choice == "6":
                    result = num1 ** num2
                    expression = f"{num1} ^ {num2} = {result}"

                elif choice == "7":
                    if num2 == 0:
                        print("❌ Floor division by zero!")
                        continue
                    result = num1 // num2
                    expression = f"{num1} // {num2} = {result}"

                else:
                    print("❌ Invalid choice!")
                    continue

            print("✅ Result:", result)
            history.append(expression)

        except ValueError:
            print("❌ Invalid input! Numbers only.")


# Run calculator
calculator()

>>>>>>> def49201bf93ed5fdd30c26a8ff520a53557464d
