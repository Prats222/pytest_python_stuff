#####################
# 1) Welcome + Real-World Circle Example
#    Scenario: Calculate the area of a circular practice turf (e.g., mini football training ring)
#####################
from math import pi
import random

print(" Welcome to the Operations & Utilities Toolkit!")

# Circular practice turf radius in meters
PRACTICE_TURF_RADIUS_M = 18  # e.g., a small circular practice area
turf_area = pi * (PRACTICE_TURF_RADIUS_M ** 2)
print(f"Area of circular practice turf (radius {PRACTICE_TURF_RADIUS_M} m): {turf_area:.2f} m²")

# Simple user interaction
user_name = input("Please enter your name: ").strip()
print(f"Hello, {user_name}! Let's get productive.\n")

#####################
# 2) Variables, Data Types, Lists, and Dictionary (Real-World: Customer & Order)
#####################
customer_name = "John Doe"
welcome_msg = "Order Processing System Ready"
note_multiline = """This console records:
- Items received
- Items dispatched
- Basic calculations"""

# Numbers
customer_age = 25
unit_price = 19.99
is_first_time_buyer = True

# Lists (inventory / menu)
fruits = ["apple", "banana", "orange"]
item_codes = [101, 102, 103, 104, 105]

# Dictionary (customer profile)
customer = {"name": "Alice", "age": 30, "city": "New York"}

print(f"Customer: {customer_name}, Age: {customer_age}")
print(f"Fruits in stock: {fruits}")
print(f"Customer profile: {customer}\n")

#####################
# 3) Arithmetic and String Operations (Real-World: Invoice arithmetic demo)
#####################
a, b = 10, 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b:.2f}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Exponent: {a} ** {b} = {a ** b}")
print(f"Modulus: {a} % {b} = {a % b}")

first_name, last_name = "John", "Doe"
full_name = f"{first_name} {last_name}"
print(f"Full name (billing contact): {full_name}")
print(f"Uppercase label: {full_name.upper()}")
print(f"Name length: {len(full_name)}\n")

#####################
# 4) If-Elif-Else Conditions (Real-World: Facility messages, driving eligibility, performance band)
#####################
ambient_temp_c = 25

if ambient_temp_c > 30:
    print(" High temperature alert: Switch on cooling!")
elif ambient_temp_c > 20:
    print(" Ambient temperature is pleasant.")
elif ambient_temp_c > 10:
    print("Slightly cool: light ventilation recommended.")
else:
    print("Cold: heating may be required.")

age = 18
has_license = True
print("Vehicle rental permitted" if age >= 18 and has_license else "Vehicle rental not permitted")

score = 85
if score >= 90:
    band = "A"
elif score >= 80:
    band = "B"
elif score >= 70:
    band = "C"
elif score >= 60:
    band = "D"
else:
    band = "F"
print(f"Performance score: {score}, Band: {band}\n")

#####################
# 5) Loops (For and While) — Real-World: IDs, menus, simple tables, countdowns
#####################
print("Processing order IDs 1 to 5:")
for i in range(1, 6):
    print(f"• Processed Order ID: {i}")

print("\nMenu items available:")
for item in ["Tea", "Coffee", "Sandwich"]:
    print(f"- {item}")

print("\nQuantity price table for unit price = 5:")
for qty in range(1, 11):
    print(f"{qty} × 5 = {5 * qty}")

print("\nDeployment countdown:")
count = 5
while count:
    print(count)
    count -= 1
print(" Deployed!\n")

print("Ticket queue (1–10), skip #5 and stop at #8:")
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(f"Ticket #{i}")

#####################
# 6) Functions — Real-World: Greetings, floor area, profiles, round plot stats
#####################
def greet(person: str) -> str:
    return f"Welcome, {person}! Your workspace is ready."


def calculate_floor_area(length_m: float, width_m: float) -> float:
    # Real-world rectangle example: Football ground (simplified rectangle)
    return length_m * width_m


def introduce_employee(name: str, age: int, city: str = "Unknown") -> str:
    return f"Employee -> Name: {name}, Age: {age}, City: {city}"


print(greet("Alice"))
# Example football ground size (training ground), e.g., 100m × 64m (illustrative)
print(f"Football ground floor area: {calculate_floor_area(100, 64)} m²")
print(introduce_employee("Bob", 25))
print(introduce_employee("Charlie", 30, "London"))


def round_plot_calculations(radius_m: float):
    # Real-world circle: round fountain / circular park / practice ring
    diameter = 2 * radius_m
    circumference = 2 * pi * radius_m
    area = pi * (radius_m ** 2)
    return diameter, circumference, area


d, c, a_val = round_plot_calculations(7)
print(f"Round plot (r=7 m): Diameter={d} m, Perimeter={c:.2f} m, Area={a_val:.2f} m²\n")

#####################
# 7) List Operations — Real-World: Stock levels, combined inventory, slicing for reports
#####################
stock_levels = [1, 2, 3, 4, 5]
print(f"Initial stock levels: {stock_levels}")

stock_levels.append(6)
stock_levels.insert(0, 0)
print(f"After restock ops: {stock_levels}")

# Safely remove a level if present
if 3 in stock_levels:
    stock_levels.remove(3)

last_removed = stock_levels.pop()
print(f"After removals: {stock_levels}")
print(f"Last removed unit level: {last_removed}")

produce = ["apple", "banana"]
vegetables = ["carrot", "potato"]
combined_inventory = produce + vegetables
print(f"Combined inventory: {combined_inventory}")

sequence = list(range(10))
print(f"First 3 IDs: {sequence[:3]}")
print(f"Last 3 IDs: {sequence[-3:]}")
print(f"Middle block: {sequence[3:7]}")
print(f"Every second ID: {sequence[::2]}")

squares = [x * x for x in range(1, 6)]
even_ids = [x for x in range(10) if x % 2 == 0]
print(f"Quality check squares: {squares}")
print(f"Even ID list: {even_ids}\n")

#####################
# 8) File Handling — Real-World: Operational log
#####################
log_file = "operations_log.txt"

with open(log_file, "w", encoding="utf-8") as f:
    f.writelines(
        [
            "LOG: System initialized\n",
            "LOG: Warehouse shift A started\n",
            "LOG: Inventory check complete\n",
        ]
    )
print("Operational log written.")

print("\nReading full log:")
with open(log_file, "r", encoding="utf-8") as f:
    print(f.read())

print("Reading log line by line:")
with open(log_file, "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, 1):
        print(f"Line {line_number}: {line.strip()}")

with open(log_file, "a", encoding="utf-8") as f:
    f.write("LOG: Shift A closed and handed over to Shift B\n")

print("\nLog after appending:")
with open(log_file, "r", encoding="utf-8") as f:
    print(f.read())

#####################
# 9) Simple Calculator — Real-World: Quick billing math
#####################
def calculator():
    try:
        num1 = float(input("Enter first amount: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second amount: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operator!")
            return

        print(f"Result: {num1} {operator} {num2} = {result}")
    except ValueError:
        print("Please enter valid numbers!")


calculator()

#####################
# 10) Number Guessing Game — Real-World: Guess the stock count
#####################
def guessing_game():
    secret_number = random.randint(1, 100)  # hidden stock level in a bin
    attempts = 0
    max_attempts = 7

    print("\n🧩 Guess the Stock Count!")
    print(f"(Hidden stock in a bin is 1–100. You have {max_attempts} attempts.)")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher count.")
            elif guess > secret_number:
                print("Too high! Try a lower count.")
            else:
                print(f" Correct! You found it in {attempts} attempts.")
                return
        except ValueError:
            print("Please enter a valid number!")

    print(f"Out of attempts! The actual stock was {secret_number}.")


guessing_game()

#####################
# 11) Todo List Manager — Real-World: Project Task Manager
#####################
def todo_manager():
    todos = []

    while True:
        print("\n=== PROJECT TASK MANAGER ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            if not todos:
                print("No tasks yet!")
            else:
                print("\nYour Tasks:")
                for i, todo in enumerate(todos, 1):
                    status = "✓" if todo["completed"] else " "
                    print(f"{i}. [{status}] {todo['task']}")

        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                todos.append({"task": task, "completed": False})
                print(f"Added: {task}")
            else:
                print("Task cannot be empty!")

        elif choice == "3":
            if not todos:
                print("No tasks to remove!")
                continue
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos.pop(index)
                    print(f"Removed: {removed['task']}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":
            if not todos:
                print("No tasks to mark!")
                continue
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(todos):
                    todos[index]["completed"] = True
                    print(f"Marked as completed: {todos[index]['task']}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "5":
            print(" Exiting Task Manager. Stay organized!")
            break

        else:
            print("Invalid choice! Please enter 1-5.")


todo_manager()
