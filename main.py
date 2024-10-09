import tkinter as tk
from tkinter import ttk

'''
Main function
'''
def main():
    print("Running Calculator...")
    # Run the window main loop
    window.mainloop()

'''
Begin Tkinter GUI code
'''
# Create the main calculator window
window = tk.Tk()
window.title("ChrisJ Calculator")
window.geometry("400x500")
window.resizable(False, False)
window.configure(bg="#2f3339") # Set the background color to matte dark grey

# Create the screen
## Create a Label widget with light blue background and black text
screen = tk.Label(window, text="9", bg="light blue", fg="black", font=("Arial", 30), width=25, height=2, anchor="e", padx=15)

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
    "0", "#", "del", "#"
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
            pass
        case "0":
            button = tk.Button(buttons_frame, text=button_text, font=("Arial", 15), width=12, height=2)
            button.grid(row=row, column=column, columnspan=2, padx=0, pady=5)
        case _:
            button = tk.Button(buttons_frame, text=button_text, font=("Arial", 15), width=5, height=2)
            button.grid(row=row, column=column, padx=4, pady=3)

    # Set the color to matte grey. This works as intended because in Python, the match statement does not create a new scope.
    button.configure(bg="#404040", fg="white") 

if __name__ == "__main__":
    main()