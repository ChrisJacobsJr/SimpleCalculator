import tkinter as tk
from tkinter import ttk
from enum import Enum

# Glboal var to store the value to be displayed on the calculator
display_value = "0"

# display_value is stored here when the user presses an operation button (+, -, *, /)
stored_value = ""

# flag to determine if the calculator has just produced an answer
result_flag = False

# Enum class to determine if the calculator is adding, subtracting, multiplying, or dividing
class Operation(Enum):
    ADDING = 1
    SUBTRACTING = 2
    MULTIPLYING = 3
    DIVIDING = 4
    NONE = 0

# Flag to determine if the calculator is currently adding, subtracting, multiplying, or dividing
current_operation = Operation.NONE


def main():
    print("Running Calculator...")
    # Run the window main loop
    window.mainloop()

def close_window():
    window.destroy()

#region Calculator functions
'''
This function is called when one of the calculator buttons are clicked.
It delegates to the appropriate function based on the button clicked, and then
updates the screen.

@param button: The string value of the button that was clicked
@return: None
'''
    #region delegation
def button_press(button):
    print("button ", button, " clicked")
    match button:
        case "clear":
            clear_screen()
        case "/":
            operation("/")
        case "*":
            operation("*")
        case "-":
            operation("-")
        case "+":
            operation("+")
        case "=":
            calculate()
        case ".":
            decimal()
        case _:         # Make sure that the button is a digit if it's not the above symbols.
            if isinstance(button, str) and button.isdigit() and len(button) == 1:
                add_to_screen(button)
            else:
                raise ValueError(f"Invalid button: {button}")
    pass

    # update_display()

    #endregion delegation

    #region screen manipulation
def clear_screen():
    global display_value, current_operation
    print("Clearing screen")
    display_value = "0"
    update_display()
    current_operation = Operation.NONE
    pass

def operation(op_str):
    global display_value, stored_value, current_operation
    operations = {
        "/": Operation.DIVIDING,
        "*": Operation.MULTIPLYING,
        "-": Operation.SUBTRACTING,
        "+": Operation.ADDING
    }
    # If current_operation is NONE, then set the flag, store the display value, and return.
    if current_operation == Operation.NONE:
        if op_str in operations:
            current_operation = operations[op_str]
            store_display_value()
        else:
            raise ValueError(f"Invalid operation: {op_str}")
        return
    else:
        # If current_operation is not NONE, then do the following:
        # Run the calculate function
        # Run this function recursively with the new operation
        calculate()
        operation(op_str)
        
        return

def calculate():
    print("Calculating")
    # Based on the operation flag, call the appropriate helper function
    # to calculate the result of the operation
    global display_value, stored_value, current_operation, result_flag

    match current_operation:
        case Operation.DIVIDING:
            result = divide(float(stored_value), float(display_value))
        case Operation.MULTIPLYING:
            result = multiply(float(stored_value), float(display_value))
        case Operation.SUBTRACTING:
            result = subtract(float(stored_value), float(display_value))
        case Operation.ADDING:
            result = add(float(stored_value), float(display_value))
        case Operation.NONE:
            return
        case _:
            raise ValueError("Invalid operation", current_operation)

    # Check if the result is a whole number
    if result.is_integer():
        display_value = str(int(result))
    else:
        display_value = str(result)

    update_display()
    current_operation = Operation.NONE
    result_flag = True

def decimal():
    print("Decimal")
    global display_value
    if '.' not in display_value:
        display_value += '.'
    update_display()


def add_to_screen(value):
    global display_value, result_flag
    print("Adding ", value, " to screen")
    if result_flag == True:
        display_value = "0"
        result_flag = False

    if display_value == '0':
        if value != '0' or current_operation != Operation.NONE:
            display_value = value
        else:
            display_value += value
    else:
        display_value += value
    update_display()

def update_display():
    screen.config(text=display_value)

    #endregion screen manipulation

#endregion Calculator functions

#region Helper functions


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def store_display_value():
    global display_value, stored_value
    stored_value = display_value
    display_value = "0"

#endregion Helper functions



'''
Begin GUI creation code
'''
#region GUI creation code

# Create the main calculator window
window = tk.Tk()
window.title("ChrisJ Calculator")
window.geometry("400x500")
window.resizable(False, False)
window.configure(bg="#2f3339") # Set the background color to matte dark grey

# Bind the Escape key to close the window
window.bind('<Escape>', lambda event: close_window())

# Create the screen
## Create a Label widget with light blue background and black text
screen = tk.Label(window, text="0", bg="light blue", fg="black", font=("Arial", 30), width=25, height=2, anchor="e", padx=15)

## Place the screen in the window
screen.pack(pady=10, padx=10)

# Create the buttons frame
buttons_frame = tk.Frame(window)
buttons_frame.pack(pady=10, padx=10)
buttons_frame.configure(bg="#707070") # Set the color to matte light grey

# Create the buttons
## Create a list of buttons for a 4x5 grid. # is a placeholder for an empty space
buttons = [
    "clear", "/", "*", "-",
    "7", "8", "9", "+",
    "4", "5", "6", "#",
    "1", "2", "3", "=",
    "0", "#", ".", "#"
]

## Place the buttons in the grid
for i, button_text in enumerate(buttons):
    row = i // 4
    column = i % 4
    match button_text:  # In Python, the match statement does not create a new scope.
        case "=" | "+":
            button = tk.Button(buttons_frame, text=button_text, font=("Arial", 23), width=3, height=3)
            button.grid(row=row, column=column, rowspan=2, padx=5, pady=0)
        case "#":
            continue # Skip palceholder buttons
        case "0":
            button = tk.Button(buttons_frame, text=button_text, font=("Arial", 15), width=12, height=2)
            button.grid(row=row, column=column, columnspan=2, padx=0, pady=5)
        case _:
            button = tk.Button(buttons_frame, text=button_text, font=("Arial", 15), width=5, height=2)
            button.grid(row=row, column=column, padx=4, pady=3)

    # Set the color to matte grey. This works as intended because in Python, the match statement does not create a new scope.
    button.configure(bg="#404040", fg="white", command=lambda btn=button_text: button_press(btn)) 

#endregion GUI creation code
'''
End GUI creation code
'''

if __name__ == "__main__":
    main()