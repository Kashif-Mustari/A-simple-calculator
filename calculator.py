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