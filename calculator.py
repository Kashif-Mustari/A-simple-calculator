<<<<<<< HEAD
import math
import time

class PowerfulCalculator:
    def __init__(self):
        self.memory = 0
        self.history = []
        self.mode = "Degrees"  # Scene 5: Degree/Radian mode

    def display_scene(self, scene_title, content):
        """Scene 8: Simple, clean, and user-friendly interface"""
        print(f"\n--- {scene_title.upper()} ---")
        for line in content:
            print(f"🎬 {line}")
            time.sleep(0.3) # Subtle delay for professional feel
        print("-" * 30)

    def show_about(self):
        # Integrating your Script Scenes into the Program
        scenes = {
            "Introduction": ["In today's modern world, a calculator is an essential tool.", 
                             "From simple arithmetic to complex scientific calculations."],
            "Purpose": ["Provides fast, accurate, and easy calculations in one place."],
            "Features": ["Supports Basic (+,-,*,/), Advanced (√, ^, !, |x|),", 
                         "and Scientific (sin, cos, tan, log, π) functions."],
            "System": ["Equipped with a Memory System and robust Error Handling."]
        }
        for title, text in scenes.items():
            self.display_scene(title, text)

    def calculate(self):
        print("⚡ Welcome to the Powerful Calculator Pro ⚡")
        print("Type 'about' to see the project script or 'help' for commands.")

        while True:
            print(f"\n[ Mode: {self.mode} | Memory: {self.memory} ]")
            choice = input("Enter Operation (e.g., +, sin, log, mem, mode, exit): ").lower().strip()

            try:
                # Scene 9: Conclusion / Exit
                if choice == 'exit':
                    print("\nConclusion: This powerful calculator is a complete and efficient digital tool.")
                    print("Thank you for using it. Goodbye!")
                    break

                if choice == 'about':
                    self.show_about()
                    continue

                # Scene 5 & 4: Scientific & Advanced Functions
                if choice in ['sin', 'cos', 'tan', 'sqrt', 'log', 'fact', 'abs']:
                    val = float(input("Enter number: "))
                    
                    if choice == 'sqrt': 
                        if val < 0: raise ValueError("Cannot square root a negative number.")
                        res, op = math.sqrt(val), f"√{val}"
                    elif choice == 'abs': # Scene 4: Absolute Value
                        res, op = abs(val), f"|{val}|"
                    elif choice == 'fact': # Scene 4: Factorial
                        res, op = math.factorial(int(val)), f"{val}!"
                    elif choice == 'log':
                        res, op = math.log10(val), f"log10({val})"
                    elif choice == 'sin':
                        res = math.sin(math.radians(val) if self.mode == "Degrees" else val)
                        op = f"sin({val})"
                    elif choice == 'cos':
                        res = math.cos(math.radians(val) if self.mode == "Degrees" else val)
                        op = f"cos({val})"
                    elif choice == 'tan':
                        res = math.tan(math.radians(val) if self.mode == "Degrees" else val)
                        op = f"tan({val})"
                
                # Scene 5: Value of Pi
                elif choice == 'pi':
                    res, op = math.pi, "π"

                # Scene 5: Mode Toggle
                elif choice == 'mode':
                    self.mode = "Radians" if self.mode == "Degrees" else "Degrees"
                    print(f"🔄 Switched to {self.mode}")
                    continue

                # Scene 6: Memory System
                elif choice == 'mem':
                    print(f"💾 Stored Memory: {self.memory}")
                    continue

                # Scene 3: Basic Operations
                elif choice in ['+', '-', '*', '/', '%', '^']:
                    n1 = float(input("First number: "))
                    n2 = float(input("Second number: "))
                    if choice == '+': res = n1 + n2
                    elif choice == '-': res = n1 - n2
                    elif choice == '*': res = n1 * n2
                    elif choice == '/': 
                        if n2 == 0: raise ZeroDivisionError("Scene 7: Cannot divide by zero!")
                        res = n1 / n2
                    elif choice == '%': res = n1 % n2
                    elif choice == '^': res = n1 ** n2
                    op = f"{n1} {choice} {n2}"

                else:
                    print("❓ Unknown command. Type 'help' for options.")
                    continue

                # Display Result
                print(f"✅ Result: {res}")
                self.memory = res # Scene 6: Storing result

            # Scene 7: Error Handling
            except ZeroDivisionError as e:
                print(f"❌ Error: {e}")
            except ValueError as e:
                print(f"❌ Error: {e} (Please enter valid numbers)")
            except Exception as e:
                print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    calc = PowerfulCalculator()
    calc.calculate()
=======
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
>>>>>>> 501046bd4f1c396a5df52beafd1adf4b167a0f90
